from rest_framework import serializers
from .models import Order, OrderItem
from inventory.serializers import ItemSerializer
from inventory.models import Item




from rest_framework import serializers
from .models import OrderItem

from rest_framework import serializers
from .models import OrderItem

from rest_framework import serializers
from .models import OrderItem

from rest_framework import serializers
from .models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    item_reference = serializers.CharField()  # Assuming item_reference is a field in the OrderItem model

    class Meta:
        model = OrderItem
        fields = ['item_reference', 'quantity']

    def create(self, validated_data):
        item_reference = validated_data.pop('item_reference')
        quantity = validated_data.pop('quantity')
        
        # You should handle the creation of OrderItem instances according to your logic

        return OrderItem.objects.create(item_reference=item_reference, quantity=quantity)


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
