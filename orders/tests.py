from django.test import TestCase
from django.utils import timezone
from .models import Order, OrderItem
from inventory.models import Item

class OrderModelTestCase(TestCase):
    def setUp(self):
        self.item1 = Item.objects.create(reference='ABC123', name='Item 1', description='Description 1', price_without_taxes=10.00, tax_rate=0.10)
        self.item2 = Item.objects.create(reference='DEF456', name='Item 2', description='Description 2', price_without_taxes=20.00, tax_rate=0.15)
        
    def test_order_creation(self):
        order = Order.objects.create(total_price_without_taxes=100.00, total_price_with_taxes=110.00)
        order.items.add(self.item1, through_defaults={'quantity': 2})
        order.items.add(self.item2, through_defaults={'quantity': 3})

        self.assertEqual(order.total_price_without_taxes, 100.00)
        self.assertEqual(order.total_price_with_taxes, 110.00)

        # Check if items are associated with the order
        self.assertEqual(order.items.count(), 2)

        # Check if order item quantities are correct
        order_item1 = order.orderitem_set.get(item=self.item1)
        self.assertEqual(order_item1.quantity, 2)

        order_item2 = order.orderitem_set.get(item=self.item2)
        self.assertEqual(order_item2.quantity, 3)

    def test_order_total_price_with_taxes_calculation(self):
        order = Order.objects.create(total_price_without_taxes=100.00)
        order.items.add(self.item1, through_defaults={'quantity': 2})
        order.items.add(self.item2, through_defaults={'quantity': 3})

        # Total price with taxes should be calculated automatically
        self.assertAlmostEqual(order.total_price_with_taxes, 110.00)

class SignalHandlerTestCase(TestCase):
    def setUp(self):
        self.item1 = Item.objects.create(reference='ABC123', name='Item 1', description='Description 1', price_without_taxes=10.00, tax_rate=0.10)
        self.item2 = Item.objects.create(reference='DEF456', name='Item 2', description='Description 2', price_without_taxes=20.00, tax_rate=0.15)

    def test_update_order_total_price_with_taxes_signal(self):
        order = Order.objects.create(total_price_without_taxes=100.00)
        order.items.add(self.item1, through_defaults={'quantity': 2})
        order.items.add(self.item2, through_defaults={'quantity': 3})

        # The signal handler should update the total price with taxes
        order.refresh_from_db()
        self.assertAlmostEqual(order.total_price_with_taxes, 110.00)

        # Adding another item should trigger the signal and update the total price with taxes
        item3 = Item.objects.create(reference='GHI789', name='Item 3', description='Description 3', price_without_taxes=15.00, tax_rate=0.12)
        order.items.add(item3, through_defaults={'quantity': 1})
        order.refresh_from_db()
        self.assertAlmostEqual(order.total_price_with_taxes, 125.00)
