from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .decorators import seller_required
from products.models import Product
from accounts.models import Seller,User
from cart.models import OrderItem, Order
from .forms import AddProductForm, ModifyProductForm
from django import forms

@login_required
@seller_required
def seller_dashboard(request):
    return render(request, '../templates/seller/dashboard.html')

def seller_products(request, pk):
    products = Product.objects.filter(seller=pk) 
    context={
        'products' : products
    }
    return render(request, '../templates/seller/products.html', context)

def seller_orders(request):
    return render(request, '../templates/seller/orders.html')

def seller_settings(request):
    return render(request, '../templates/seller/settings.html')

def seller_edit_profile(request):
    return render(request, '../templates/seller/edit_profile.html')

def seller_add_product(request):
    return render(request, '../templates/seller/add_product.html')

def seller_modify_product(request,  seller, pk):
   
    product = Product.objects.get(id=pk)
    form = AddProductForm(instance=product)
    user = get_object_or_404(User, pk=seller)
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = user
            product.save()
            return redirect('../templates/seller/dashboard.html', seller=user.pk)
    context = {
        'form': form
    }
    return render(request, '../templates/seller/modify.html', context)


@login_required
@seller_required
def add_product(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = user
            product.save()
            return render(request, '../templates/seller/dashboard.html')
    else:
        form = AddProductForm()

    return render(request, '../templates/seller/add_product.html',{'form': form})

