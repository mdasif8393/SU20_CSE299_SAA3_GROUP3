from django.shortcuts import render
from sslcommerz_lib import SSLCOMMERZ
from django.http import JsonResponse
from .models import Order, OrderItem
from products.models import Product
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from accounts.models import Customer, User, Seller
from .cart import Cart
from .forms import CartAddProductForm
#import pycurl 

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

'''def checkout(request):
    #settings = { 'store_id': 'bookr5f41517d60625', 'store_pass': 'bookr5f41517d60625@ssl', 'issandbox': True }
    #sslcommez = SSLCOMMERZ(settings)
    #sessionkey = 'A8EF93B75B8107E4F36049E80B4F9149'
    post_body = {}
    post_data['store_id'] = "bookr5f41517d60625";
    post_data['store_passwd'] = "bookr5f41517d60625@ssl";
    post_body['tran_id'] = '5E121A0D01F92'
    post_body['val_id'] = '200105225826116qFnATY9sHIwo'
    post_data['success_url'] = "http://localhost/book_rental/public/success.py";
    post_data['fail_url'] = "http://localhost/new_sslcz_gw/fail.py";
    post_data['cancel_url'] = "http://localhost/new_sslcz_gw/cancel.py";
    post_body['amount'] = "10.00"
    post_body['card_type'] = "VISA-Dutch Bangla"
    post_body['store_amount'] = "9.75"
    post_body['card_no'] = "418117XXXXXX6675"
    post_body['bank_tran_id'] = "200105225825DBgSoRGLvczhFjj"
    post_body['status'] = "VALID"
    post_body['tran_date'] = "2020-01-05 22:58:21"
    post_body['currency'] = "BDT"
    post_body['card_issuer'] = "TRUST BANK, LTD."
    post_body['card_brand'] = "VISA"
    post_body['card_issuer_country'] = "Bangladesh"
    post_body['card_issuer_country_code'] = "BD"
    post_body['store_id'] = "bookr5f41517d60625"
    post_body['currency_type'] = "BDT"
    post_body['currency_amount'] = "10.00"
    post_body['currency_rate'] = "1.0000"
    post_body['base_fair'] = "0.00"
    post_body['risk_level'] = "0"
    post_body['risk_title'] = "Safe"

    handle = pycurl.Curl() 
    handle.setopt(pycurl.URL, "https://sandbox.sslcommerz.com/gwprocess/v3/api.php")
    handle.setopt(pycurl.CONNECTTIMEOUT, 30)
    handle.setopt(pycurl.TIMEOUT, 30)
    handle.setopt(pycurl.POST, 1 )
    handle.setopt(pycurl.POSTFIELDS, post_body)
    handle.setopt(pycurl.RETURNTRANSFER, True)
    handle.setopt(pycurl.SSL_VERIFYPEER, False)

    content = handle.perform()
    code = handle.getinfo(pycurl.HTTP_CODE)

    if code == 200 and not handle.errno():
       handle.close()
	   sslcommerzResponse = content
    else :
	    handle.close()
	    exit;

    response = sslcommez.hash_validate_ipn(post_body)
    print(response)
    return response'''