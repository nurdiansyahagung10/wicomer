from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Address,Store
from product.models import product
# Create your models here.
class Order(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    buyer_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    address_buyer = models.ForeignKey(Address, on_delete=models.CASCADE)
    quantity_order = models.IntegerField()
    total_price = models.IntegerField()
    pre_order_time = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(product, on_delete= models.CASCADE)
    spesification = models.CharField(max_length = 100)
    spesificationvalue = models.CharField(max_length = 100)    
    notes_product = models.TextField(null = True)
    notes_address = models.TextField(null = True)
    shipping_information = models.CharField(max_length = 100, default = 'Waiting Seller Approved')
    created_at = models.DateTimeField(auto_now_add = "true")
    updated_at = models.DateTimeField(auto_now = "true")