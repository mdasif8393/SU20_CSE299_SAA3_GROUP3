from django.contrib import admin
from .models import Wish_list, Favourite
from accounts.models import User,Customer,Seller
from products.models import Product, Review

# Register your models here.

admin.site.register(Wish_list)
admin.site.register(Favourite)