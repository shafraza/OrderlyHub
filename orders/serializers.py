from rest_framework import serializers
from .models import Order, OrderItem
from inventory.serializers import ItemSerializer
from inventory.models import Item
from rest_framework import serializers
from .models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    item_reference = serializers.CharField(source='item.reference')  # Access the reference field of the related Item model

    class Meta:
        model = OrderItem
        fields = ['item_reference', 'quantity']

    def create(self, validated_data):
        item_reference = validated_data.pop('item_reference')
        quantity = validated_data.pop('quantity')
        
        # You should handle the creation of OrderItem instances according to your logic
        
        item = get_object_or_404(Item, reference=item_reference)
        return OrderItem.objects.create(item=item, quantity=quantity)

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price_without_taxes = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    total_price_with_taxes = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)

    class Meta:
        model = Order
        fields = ['total_price_without_taxes', 'total_price_with_taxes', 'items']
