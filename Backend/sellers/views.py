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

def add_product(request):
    if request.method == 'POST':
         form = AddProductForm(request.POST, request.FILES)
         if form.is_valid():
            form.seller_id = User.objects.get(id=request.user.id)
            form.save()
            return redirect('seller/seller_dashboard.html')
    else:
        form = AddProductForm()

    return render(request, 'seller/seller_dashboard.html')