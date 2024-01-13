from django.db import models
from django.contrib.auth.models import AbstractUser

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
        