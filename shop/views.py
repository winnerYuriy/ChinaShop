from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from .forms import ProductSearchForm



def search_products(request):
    query = request.GET.get('query')

    if query:
        results = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        total_results = results.count()
        return render(request, 'search_results.html', {'results': results, 'total_results': total_results, 'query': query})
    else:
        # Handle the case when query is None or empty
        return render(request, 'error_template.html', {'error_message': 'Invalid search query'})




def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)




def catalog(request):
    parent_categories = Category.objects.filter(parent_category=None)
    sub_categories = Category.objects.filter(parent_category__isnull=False)
    context = {'parent_categories': parent_categories, 'sub_categories': sub_categories}
    return render(request, 'catalog.html', context)
    

def products_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {'category': category, 'products': products}
    return render(request, 'products_by_category.html', context)


def products_by_subcategory(request, category_slug, sub_category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    sub_category = get_object_or_404(Category, slug=sub_category_slug, parent_category=category)
    products = Product.objects.filter(category=sub_category)
    context = {'category': category, 'sub_category': sub_category, 'products': products}
    return render(request, 'products_by_subcategory.html', context)

def product_details (request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {'product': product}
    return render(request, 'product_details.html', context)
