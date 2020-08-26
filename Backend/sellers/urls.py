from django.urls import path
from .import views

urlpatterns = [
    path('seller_dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('add_product/', views.add_product, name='add_product'),
]