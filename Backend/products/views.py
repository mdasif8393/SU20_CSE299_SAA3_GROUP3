from django.shortcuts import render, get_object_or_404
from .models import Product, Review
from accounts.models import User
from .forms import ReviewForm

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


def single_product(request, pk, id):
    product = Product.objects.filter(id=pk)
    customer = User.objects.filter(id=id)
    reviews = Review.objects.all()
    user_review = Review.objects.all()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.customer = user
            review.product = product
            review.save()
            return redirect('../templates/products/single_product.html', pk=user.pk)
    else:
        form = ReviewForm()
    context={
        'product': product,
        'form'   :form,
        'reviews' : reviews,
    }
    return render(request, 'products/single_product.html',context)

'''def add_review(request):
    #user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            #product.seller = user
            product.save()
            return redirect('../templates/products/single_product.html', pk=user.pk)
    else:
        form = ReviewForm()

    return render(request, '../templates/products/single_product.html',{'form': form})'''
