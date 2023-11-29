from django.shortcuts import render, get_object_or_404
from shop.models import *

def index(request):
    #softs = Soft.objects.all()
    categories = Category.objects.filter(parent_category=None)
    products = Product.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, 'index.html', context)
    

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop.html', context)

def actions(request):
    products = Product.objects.filter(status_id=2)
    context = {'products': products}
    return render(request, 'actions.html', context)
    
def about(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'about.html', context)

def contacts(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'contacts.html', context)

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)

def repair(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'repair.html', context)


def brands(request):
    brands = Brand.objects.all()
    context = {'brands': brands}
    return render(request, 'brands.html', context)

def products_by_brand(request, brand_slug):
    brand = get_object_or_404(Brand, slug=brand_slug)
    products = Product.objects.filter(brand=brand, )
    context = {'brand': brand, 'products': products}
    return render(request, 'products_by_brand.html', context)