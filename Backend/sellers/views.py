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
from .forms import AddProductForm
from django import forms

@login_required
@seller_required
def seller_dashboard(request):
    return render(request, 'seller/seller_dashboard.html')

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
            return redirect('../templates/seller/seller_dashboard.html', pk=user.pk)
    else:
        form = AddProductForm()

    return render(request, '../templates/seller/add_product.html',{'form': form})

@login_required
@seller_required
def show_products(request,pk):

    products = Product.objects.filter(seller=pk) 
    context={
        'products' : products
    }
    return render(request, '../templates/seller/your_products.html', context)
