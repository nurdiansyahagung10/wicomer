from django.db import models
from accounts.models import Store
# Create your models here.

class product(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    name_product = models.CharField(max_length=100, unique=True)
    description_product = models.TextField()
    CATEGORY_CHOICES = (
        ('', ''),
        ('food', 'Food'),
        ('drink', 'Drink'),
        ('fruit', 'Fruit'),
        ('ice_cream', 'Ice Cream'),
        ('raw_food', 'Raw Food'),
        ('man_clothes', 'Man Clothes'),
        ('man_accesories', 'Man Accesories'),
        ('woman_clothes', 'Woman Clothes'),
        ('woman_accesories', 'Woman Accesories'), 
        ('hat', 'Hat'),
        ('shoes', 'Shoes'),
        ('motorcycle_and_accesories', 'Motorcycle and Accesories'),
        ('car_and_accesories', 'Car and Accesories'),
        ('helmet_and_accesories', 'Helmet and Accesories'),
        ('electronic', 'Electronic'),
        ('handphone_and_accesories', 'Handphone and Accesories'),
        ('laptop_and_accesories', 'Laptop and Accesories'),
        ('computer_and_accesories', 'Computer and Accesories'),
        ('skincare', 'Skincare'),
        ('makeup', 'Makeup'),
        ('basic_needs', 'Basic Needs'),
        ('voucher_and_phonecredit', 'Voucher and Phonecredit'),
        ('top_up_games', 'Top Up Games'),
        ('home_decoration', 'Home Decoration')
    )
    category_product = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='')    
    price_product = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_product = models.IntegerField(default = 0)
    total_sales = models.IntegerField(default = 0)
    KIND_CHOICHES = (
        ('', ''),
        ('new', 'New'),
        ('former', 'Former'),
    )
    kind = models.CharField(max_length=50, choices=KIND_CHOICHES, default='')
    pre_order_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name_product

class ProductSpesification(models.Model):
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    name_Spesification = models.CharField(max_length=50)
    def __str__(self):
        return self.name_Spesification

class SpesificationValue(models.Model):
    spesification_id = models.ForeignKey(ProductSpesification, on_delete=models.CASCADE)
    name_value = models.CharField(max_length=50)
    def __str__(self):
        return self.name_value

class ProductImage(models.Model):
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    name_image = models.ImageField(upload_to='product_images/')

    def __str__(self):
            return f"Image for {self.product_id.name_product}"