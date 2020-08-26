from django.shortcuts import render
from .models import Product

# Create your views here.

def products(request):
    products = Product.objects.all()
    context={
        'products': products,
    }
    return render(request, 'products/products.html', context)

def custom_search(request):

    if request.method == 'GET':
        category = request.GET['category'] 
        min_price = request.GET.get('min', 0)
        max_price = request.GET.get('max', 0)
        product = Product.objects.filter(category__iexact=category)
        product =product.filter(price__range=(min_price, max_price))
    context= {
        'product' : product,
    }

    return render(request, 'products/products.html', context)


def single_product(request):
    return render(request, 'products/single_product.html')
