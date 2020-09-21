from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('add/(<int:product_id>', views.cart_add, name='cart_add'),
    path('create/', views.order_create, name='order_create'),
    path('checkout/',views.checkout, name='checkout'),
    path('success/',csrf_exempt(views.success)),
]