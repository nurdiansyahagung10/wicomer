# Generated by Django 5.0.1 on 2024-02-11 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_pre_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='pre_order_time',
            new_name='pre_order_date',
        ),
    ]
