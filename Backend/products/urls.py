from django.urls import path
from .import views

urlpatterns = [
    path('product_list/', views.products, name='products'),
    path('single_product/', views.single_product, name='single_product'),
]