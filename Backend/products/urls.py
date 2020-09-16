from django.urls import path
from .import views

urlpatterns = [
    path('product_list/', views.products, name='products'),
    path('<int:pk>/single_product/<str:token>/', views.single_product, name='single_product'),
    #path('<str:token>/single_product/', views.single_product, name='single_product'),
    path('custom_search/', views.custom_search, name='custom_search'),
    #path('<int:pk>/review/', views.add_review, name='add_review'),
]