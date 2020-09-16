from django.shortcuts import render, get_object_or_404
from .models import Product, Review
from accounts.models import User
from customers.models import Wish_list, Favourite
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from cart.forms import CartAddProductForm

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


def single_product(request, pk=None, token=None):
    product = get_object_or_404(Product, pk=pk)
    #product = Product.objects.get(id=pk)
    reviews = product.reviews.all()
    cart_product_form = CartAddProductForm()
    if request.user.id is not None:
       user = get_object_or_404(User, id=request.user.id)
       #if user presses wish list button
       if token == 'wish':
           wish = Wish_list(product=product, customer=user)
           wish.save()
           form = ReviewForm()
           context={
                    'product': product,
                    'form': form,
                    'reviews':reviews,
                    'cart_product_form': cart_product_form,
                }
           return render(request, '../templates/products/single_product.html',context)
       if token == 'favourite':
           favourite = Favourite(product=product, customer=user)
           favourite.save()
           form = ReviewForm()
           context={
                    'product': product,
                    'form': form,
                    'reviews':reviews,
                    'cart_product_form': cart_product_form,
                }
           return render(request, '../templates/products/single_product.html',context)
       if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.customer = user
                review.save()
                reviews = product.reviews.all()
                form = ReviewForm()
                context={
                        'product': product,
                        'form': form,
                        'reviews':reviews,
                        'cart_product_form': cart_product_form,
                    }
                return render(request, '../templates/products/single_product.html',context)
       else:
            form = ReviewForm()
       context={
            'product': product,
            'form': form,
            'reviews':reviews,
            'cart_product_form': cart_product_form,
        }
       return render(request, '../templates/products/single_product.html',context)
    context={
            'product': product,
            'reviews':reviews,
            'cart_product_form': cart_product_form,
        }
    return render(request, '../templates/products/single_product.html',context)

'''def add_review(request, pk):
    user = get_object_or_404(User, id=request.user.id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = pk
            review.customer = user
            product.save()
            return redirect('../templates/products/single_product.html')
    else:
        form = ReviewForm()

    return render(request, '../templates/products/single_product.html',{'form': form})'''


'''customer = User.objects.filter(id=pk)
    reviews = Review.objects.all()
    user_review = Product.user_review.all()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.customer = user
            review.product = product
            review.save()
            return redirect('../templates/products/single_product.html')
    else:
        form = ReviewForm()
    context={
        'product': product,
        'form'   :form,
        'reviews' : reviews,
    }'''