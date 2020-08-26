from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):
    shoes = Product.objects.filter(category__iexact='shoes')
    context= {
        'shoes' : shoes,
    }

    return render(request, '../templates/pages/index.html', context)
   



