from django.urls import path
from .import views

urlpatterns = [
    path('product_list/', views.products, name='products'),
    path('<int:pk>/single_product/<int:id>/user', views.single_product, name='single_product'),
    path('custom_search/', views.custom_search, name='custom_search'),
    #path('review/', views.add_review, name='add_review'),
]