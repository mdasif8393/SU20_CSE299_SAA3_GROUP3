from django.db import models
from django.utils import timezone
from datetime import date
from accounts.models import User, Customer
from products.models import Product

# Create your models here.

class Wish_list(models.Model):
      customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
      product  = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
      added_at = models.DateTimeField(default=timezone.now, null=True)

class Favourite(models.Model):
      customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="favourite")
      product  = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="favourite_product")
      added_at = models.DateTimeField(default=timezone.now, null=True)