from django.contrib import admin
from .models import Product, Review
from accounts.models import User

# Register your models here.

admin.site.register(Product)
admin.site.register(Review)