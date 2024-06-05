from django.urls import path
from .views import cart, add_cart_product, remove_cart_product, remove_cart_item, checkout


urlpatterns = [
    path('', cart, name='cart_page'),
    path('add_cart_product/<int:product_id>/', add_cart_product, name='add_cart_product'),
    path('remove_cart_product/<int:product_id>/<int:cart_item_id>/', remove_cart_product, name='remove_cart_product'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', remove_cart_item, name='remove_cart_item'),
    path('checkout/', checkout, name='checkout_page'),
]
