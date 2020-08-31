from django.urls import path
from .import views

urlpatterns = [
    path('seller_dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('<int:pk>/product/', views.add_product, name='add_product'),
    path('<int:pk>/your_product/', views.show_products, name='show_products'),
]