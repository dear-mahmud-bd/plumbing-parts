from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Product, ReviewRating

# Register your models here.

class ProductAdmin(ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
admin.site.register(Product, ProductAdmin)

admin.site.register(ReviewRating)
