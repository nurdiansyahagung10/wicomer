from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email_adress', max_length=255, unique=True)
    date_of_birth = models.DateField( auto_now=False, auto_now_add=False, null=True)
    first_name = None
    last_name = None
    bio = models.TextField(null=True, blank=True)
    is_seller = models.BooleanField(default= False)
    pelajar = models.BooleanField(default=False)

    def get_email(self):
        return self.email
        
    def __str__(self):
        return self.username
        
class Store(models.Model):
    store_seller_id = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    store_image = models.ImageField(upload_to='store_images/', blank=True, null=True)
    phonenumber = models.IntegerField()
    email = models.EmailField()
    store_name = models.CharField(max_length=100)
    store_description = models.TextField(null=True)
    store_open = models.TimeField()
    store_closed = models.TimeField()
    
    def __str__(self):
        return str(self.store_name)