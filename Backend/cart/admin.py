from django.contrib import admin
from .models import Order, OrderItem
from accounts.models import Customer
from products.models import Product

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'email','address', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)