from django.urls import path
from .import views

urlpatterns = [
    path('seller_dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('<int:pk>/product/', views.add_product, name='add_product'),
    #path('<int:pk>/your_product/', views.show_products, name='show_products'),
    path('<int:pk>/your_product/', views.seller_products, name='seller_products'),
    path('seller_orders/', views.seller_orders, name='seller_orders'),
    path('seller_settings/', views.seller_settings, name='seller_settings'),
    path('seller_edit_profile/', views.seller_edit_profile, name='seller_edit_profile'),
    path('seller_add_product/', views.seller_add_product, name='seller_add_product'),
    path('<int:pk>/<int:seller>/modify_product/', views.seller_modify_product, name='seller_modify_product'),
]