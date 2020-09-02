from django.shortcuts import render
from products.models import Product
from taggit.models import Tag

# Create your views here.

def index(request):
    shoes = Product.objects.filter(category__iexact='shoes')
    context= {
        'shoes' : shoes,
    }

    return render(request, '../templates/pages/index.html', context)
   
def product_category(request, pk, tag):
    tags = Tag.objects.get(name__exact=tag)
    products = Product.objects.filter(tags__exact=tags)
    context={
        'products': products,
    }
    return render(request, 'products/products.html',context)


