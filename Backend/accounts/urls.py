from django.urls import path
from .import views

urlpatterns = [
    path('customer_register/',views.CustomerSignUpView.as_view(), name='customer_register'),
    path('seller_register/',views.SellerSignUpView.as_view(), name='seller_register'),
    path('login/', views.login, name='login'),
]