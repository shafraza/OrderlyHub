from django.db import models
from inventory.models import Item
from django.db import models
from django.db.models.signals import m2m_changed
from django.db import models
from inventory.models import Item

class Order(models.Model):
    items = models.ManyToManyField(Item, through='orders.OrderItem')  # Replace 'yourapp' with your actual app label
    total_price_without_taxes = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    total_price_with_taxes = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"

def update_order_total_price_with_taxes(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        instance.save()

models.signals.m2m_changed.connect(update_order_total_price_with_taxes, sender=Order.items.through)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=1)  

    def __str__(self):
        return f"Order {self.order_id} - Item {self.item_id} - Quantity {self.quantity}"
