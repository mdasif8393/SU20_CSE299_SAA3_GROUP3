from django.shortcuts import render
from sslcommerz_lib import SSLCOMMERZ
# Create your views here.

def cart(request):
    return render(request, 'cart/cart.html')

def checkout(request):
    settings = { 'store_id': 'bookr5f41517d60625', 'store_pass': 'bookr5f41517d60625@ssl', 'issandbox': True }
    sslcommez = SSLCOMMERZ(settings)
    sessionkey = 'A8EF93B75B8107E4F36049E80B4F9149'

    post_body = {}
    post_body['tran_id'] = '5E121A0D01F92'
    post_body['val_id'] = '200105225826116qFnATY9sHIwo'
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
    response = sslcommez.hash_validate_ipn(post_body)
    print(response)
    return response