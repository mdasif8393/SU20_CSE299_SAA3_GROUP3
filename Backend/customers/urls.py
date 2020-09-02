from django.urls import path
from .import views

urlpatterns = [
    path('', views.customer_dashboard, name='customer_dashboard'),
    #path('', views.index_products, name='index_products'),
]