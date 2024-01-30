from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.product)
admin.site.register(models.ProductImage)
admin.site.register(models.SpesificationProduct)
admin.site.register(models.SpesificationValue)