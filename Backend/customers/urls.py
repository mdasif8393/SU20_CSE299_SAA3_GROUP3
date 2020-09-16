from django.urls import path
from .import views

urlpatterns = [
    path('', views.customer_dashboard, name='customer_dashboard'),
    path('orders/', views.order, name='order'),
    path('profile/', views.profile, name='profile'),
    path('wish_list/', views.wish_list, name='wish_list'),
    path('favourite/', views.favourite, name='favourite'),
]