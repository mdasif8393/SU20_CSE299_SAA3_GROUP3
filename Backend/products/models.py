from django.db import models
from django.utils import timezone
from datetime import date
from taggit.managers import TaggableManager
from accounts.models import Seller, User, Customer

class Product(models.Model):
    CATEGORY = (
                 ('Phones & Accessories', 'Phones & Accessories'),
                 ('Kitchen Tools', 'Kitchen Tools'),
                 ('Baby Products', 'Baby Products'),
                 ('Women\'s Clothing', 'Women\'s Clothing'),
                 ('Men\'s Clothing', 'Men\'s Clothing'),
                 ('Beauty, Hair & Health', 'Beauty, Hair & Health'),
                 ('Shoes','Shoes'),
                 ('Bags', 'Bags'),
                 ('Sports & Outdoors', 'Sports & Outdoors'),
                 ('Home Improvement Tools', 'Home Improvement Tools'),
                 ('Gadgets', 'Gadgets'),
               )
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="products")
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="gallery")
    uploaded_at = models.DateTimeField(default=timezone.now, null=True)
    total_units = models.IntegerField(default=1)
    tags = TaggableManager()

    class Meta:
        db_table = 'Product'
        verbose_name = "product"

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="reviews")
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="user_review")
    text = models.TextField()
    added_at = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        db_table = 'Review'
        verbose_name = "review"

    def __str__(self):
        return self.product


'''class Order(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.ForeignKey(Seller, on_delete=models.CASCADE)
    price = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="gallery")'''