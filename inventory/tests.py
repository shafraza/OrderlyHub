from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Item
from .serializers import ItemSerializer

class ItemAPITestCase(APITestCase):
    def setUp(self):
        """
        Set up test data for each test method.
        """
        # Create an item instance for testing
        self.item_data = {
            "reference": "123",
            "name": "Sample Item",
            "description": "This is a sample item.",
            "price_without_taxes": 10.99,
            "applicable_tax": 0.08
        }
        self.item = Item.objects.create(**self.item_data)

    def test_create_item(self):
        """
        Test creating a new item via API.
        """
        # Send a POST request to create a new item
        response = self.client.post(reverse('item-list'), self.item_data, format='json')
        
        # Assert that the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Assert that the number of items in the database has increased by 1
        self.assertEqual(Item.objects.count(), 2)
        
        # Assert that the last item in the database has the correct name
        self.assertEqual(Item.objects.last().name, self.item_data['name'])

    def test_retrieve_item(self):
        """
        Test retrieving an existing item via API.
        """
        # Send a GET request to retrieve the item
        response = self.client.get(reverse('item-detail', args=[self.item.pk]))
        
        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assert that the retrieved data matches the serialized item data
        self.assertEqual(response.data, ItemSerializer(self.item).data)

    def test_update_item(self):
        """
        Test updating an existing item via API.
        """
        # Define updated data for the item
        updated_data = {
            "name": "Updated Sample Item",
            "description": "Updated Description",
            "price_without_taxes": 12.99,
            "applicable_tax": 0.99,
            "reference": "456"
        }
        
        # Send a PUT request to update the item
        response = self.client.put(reverse('item-detail', args=[self.item.pk]), updated_data, format='json')
        
        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assert that the name of the updated item matches the updated data
        self.assertEqual(Item.objects.get(pk=self.item.pk).name, updated_data['name'])

    def test_delete_item(self):
        """
        Test deleting an existing item via API.
        """
        # Send a DELETE request to delete the item
        response = self.client.delete(reverse('item-detail', args=[self.item.pk]))
        
        # Assert that the response status code is 204 No Content
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Assert that there are no items left in the database
        self.assertEqual(Item.objects.count(), 0)
