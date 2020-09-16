from django.shortcuts import render
from .models import Wish_list, Favourite
from products.models import Product
from accounts.models import User, Customer
from cart.models import Order, OrderItem
# Create your views here.

def customer_dashboard(request):
    return render(request, "customers/menu.html")

def profile(request):
    user = Customer.objects.get(user=request.user)
    context ={
        'user' : user,
    }
    return render(request, "customers/profile.html", context)

def order(request):
    orders = Order.objects.filter(customer__exact=request.user.id)
    #orderItems = orders.items.all()
    context={
        'orders': orders,
    }
    return render(request, "customers/orders.html", context)

def wish_list(request):
    wish_lists = Wish_list.objects.filter(customer__exact=request.user.id)
    context={
        'wish_lists': wish_lists,
    }
    return render(request, "customers/wish_list.html", context)

def favourite(request):
    favourites = Favourite.objects.filter(customer__exact=request.user.id)
    context={
        'favourites': favourites,
    }
    return render(request, "customers/favourites.html", context)