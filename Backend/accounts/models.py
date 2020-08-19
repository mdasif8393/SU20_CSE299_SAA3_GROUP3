from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
      is_customer = models.BooleanField(default=False)
      is_seller = models.BooleanField(default=False)

      class Meta():
        db_table = 'Users'
        


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(null=True,max_length=200)
    email = models.EmailField(null=True,max_length=100)
    address = models.TextField(null=True,max_length=11)
    phone_number = models.CharField(null=True,max_length=11)
    picture = models.ImageField(null=True, blank=True, upload_to="gallery")

    class Meta:
        db_table = 'Customer'
        verbose_name = "customer"

    def __str__(self):
        return self.full_name
        
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(null=True,max_length=200)
    email = models.EmailField(null=True,max_length=200)
    address = models.TextField(null=True,max_length=11)
    phone_number = models.CharField(null=True,max_length=11)
    picture = models.ImageField(null=True, blank=True, upload_to="gallery")
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Seller'
        verbose_name = "seller"

    def __str__(self):
        return self.full_name