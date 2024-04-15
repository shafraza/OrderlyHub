from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import OrderSerializer
from inventory.models import Item
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from .models import Order, OrderItem  # Import OrderItem model


@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'POST':
        data = request.data
        items_data = data.pop('order_items', [])  # Extract items data
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            order = serializer.save()
            for item_data in items_data:
                item_reference = item_data.get('item_reference')
                quantity = item_data.get('quantity')
                item = get_object_or_404(Item, reference=item_reference)
                # Ensure item exists
                if not item:
                    raise ValidationError(f"Item with reference '{item_reference}' does not exist.")
                OrderItem.objects.create(order=order, item=item, quantity=quantity)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        order.delete()
        return Response({'message': 'Order deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
