from django.urls import path
from .views import  *

urlpatterns = [
    path('place_order/', place_order, name='place_order'),
    path('order_complete/', order_complete, name='order_complete'),
    path('payment/success/', CheckoutSuccessView.as_view(), name='success'),
] 
