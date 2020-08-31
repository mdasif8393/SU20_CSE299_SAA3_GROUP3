from django import forms
from django.utils import timezone
from datetime import date
from products.models import Product

class AddProductForm(forms.ModelForm):
      class Meta:
          model = Product
          fields=('name', 'price', 'category', 'description', 'image', 'tags')

