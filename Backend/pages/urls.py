from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:tag>/product_category/', views.product_category, name='product_category'),
]