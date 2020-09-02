from django import forms
from django.utils import timezone
from datetime import date
from products.models import Product,Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('text',)