from django.urls import path
from .views import store, product_detail, search, submit_review

urlpatterns = [
    path('', store, name='store_page'),
    path('category/<slug:category_slug>/', store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_detail_page'),
    path('search/', search, name='search'),
    path('submit_review/<int:product_id>/', submit_review, name='submit_review'),
]
