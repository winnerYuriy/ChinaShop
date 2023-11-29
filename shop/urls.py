from django.urls import path
from .views import *

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('products/', products, name='products'),
    path('products/<slug:category_slug>/', products_by_category, name='products_by_category'), 
    path('products/<slug:category_slug>/<slug:subcategory_slug>/', products_by_subcategory, name='products_by_subcategory'), 
    path('search/', search_products, name='search_products'),
    path('product/<slug:product_slug>/', product_details, name='product_details'),
]
