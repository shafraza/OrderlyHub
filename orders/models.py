from django.db import models
from inventory.models import Item

class Order(models.Model):
    items = models.ManyToManyField(Item, through='OrderItem')
    total_price_without_taxes = models.DecimalField(max_digits=10, decimal_places=2)
    total_price_with_taxes = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

