from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Cart, CartItem

# Register your models here.

class CartAdmin(ModelAdmin):
    list_display = ('cart_id', 'date_added')
admin.site.register(Cart, CartAdmin)

class CartItemAdmin(ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')
admin.site.register(CartItem, CartItemAdmin)
