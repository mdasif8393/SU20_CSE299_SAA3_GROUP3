from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext, gettext_lazy as _
from django.db import transaction
from .models import Seller, Customer, User

class CustomerSignUpForm(UserCreationForm):
    full_name=forms.CharField(required=True)
    email = forms.CharField(required=True)
    address = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    #image = forms.ImageField(null=True, blank=True, upload_to="gallery")
   
    class Meta(UserCreationForm.Meta):
          model = User
             
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.full_name=self.cleaned_data.get('full_name')
        customer.email=self.cleaned_data.get('email')
        customer.address=self.cleaned_data.get('address')
        customer.phone_number=self.cleaned_data.get('phone_number')
        customer.image=self.cleaned_data.get('image')
        customer.save()
        return user


class SellerSignUpForm(UserCreationForm):
    full_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    address = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    #image = forms.ImageField(null=True, blank=True, upload_to="gallery")

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.save()
        seller = Seller.objects.create(user=user)
        seller.full_name=self.cleaned_data.get('full_name')
        seller.email=self.cleaned_data.get('email')
        seller.address=self.cleaned_data.get('address')
        seller.phone_number=self.cleaned_data.get('phone_number')
        seller.save()
        return user


