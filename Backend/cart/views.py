from django.shortcuts import render
from sslcommerz_lib import SSLCOMMERZ
from django.http import JsonResponse
from .models import Order, OrderItem
from products.models import Product
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from products.models import Product
from accounts.models import Customer, User, Seller
from .cart import Cart
from .forms import CartAddProductForm
from django.views.decorators.csrf import ensure_csrf_cookie
import uuid
#import pycurl 
@login_required
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
        quantity=cd['quantity'],
        update_quantity=cd['update'])
        return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],'update': True})
    return render(request, 'cart/cart.html', {'cart': cart})

def order_create(request):
    customer = Customer.objects.get(user_id=request.user)
    cart = Cart(request)
    order = Order.objects.create(customer=customer, email=customer.email, address=customer.address, paid=True)
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])

    cart.clear()
    return render(request,'cart/cart.html',{'order': order})
    
@ensure_csrf_cookie
def checkout(request):
    cart = Cart(request)
    customer = Customer.objects.get(user_id=request.user)
    request.session['customer'] = customer
    settings = { 'store_id': 'bookr5f41517d60625', 'store_pass': 'bookr5f41517d60625@ssl', 'issandbox': True }
    sslcommez = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = cart.get_total_price()
    post_body['currency'] = "BDT"
    post_body['tran_id'] = "1234"
    post_body['success_url'] = "http://127.0.0.1:8000/cart/success/"
    post_body['fail_url'] = "your fail url"
    post_body['cancel_url'] = "your cancel url"
    post_body['emi_option'] = 0
    post_body['cus_name'] = "request.user"
    post_body['cus_email'] = customer.email
    post_body['cus_phone'] = customer.phone_number
    post_body['cus_add1'] = customer.address
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"
    response = sslcommez.createSession(post_body)
    return redirect(response['GatewayPageURL'])


def success(request):
    settings = { 'store_id': 'bookr5f41517d60625', 'store_pass': 'bookr5f41517d60625@ssl', 'issandbox': True }
    sslcommez = SSLCOMMERZ(settings)

    tranid = "1234"
    response = sslcommez.transaction_query_tranid(tranid)
    context={
        "response":response,
    }

    return render(request,'cart/checkout.html', context)