# Generated by Django 5.1.dev20240412151528 on 2024-04-16 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_id_alter_order_total_price_with_taxes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price_without_taxes',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]