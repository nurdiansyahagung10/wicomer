from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.

class User(AbstractUser):
    user_image = models.ImageField( upload_to='user_images/',  blank=True, null=True)
    email = models.EmailField( max_length=155, unique=True)
    date_of_birth = models.DateField(null=True)
    description = models.TextField(null=True, blank=True)
    pelajar = models.BooleanField(default=False)

    def __str__(self):
        return self.username
        
class School (models.Model):
    school_name = models.CharField(max_length=100, unique= True)
    school_class_name = models.CharField( max_length=100)
    major = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.school_name
    
class Address(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    phone_number = models.IntegerField()
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    detail_address = models.TextField(max_length=100)
    main_address = models.BooleanField(default = False)
    address_for_store = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"address of {self.user_id}"
 
class Store(models.Model):
    seller_id = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    store_image = models.ImageField(upload_to='store_images/', blank=True, null=True)
    phone_number_store = models.IntegerField(unique= True)
    email_store = models.EmailField(unique= True)
    store_name = models.CharField(max_length=100,unique= True)
    store_description = models.TextField(null=True)
    store_open_time = models.TimeField()
    store_closed_time = models.TimeField()
    open_date = models.CharField(max_length=100, null=True)
    location_store = models.ForeignKey(Address, on_delete=models.PROTECT,null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.store_name
    
