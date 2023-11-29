"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('shop/', include('shop.urls')),
    path('users/', include('users.urls',namespace='users')),
    path('products/', views.products, name='products'),
    path('actions/', views.actions, name='actions'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('store/', views.store, name='store'),
    path('repair/', views.repair, name='repair'),
    path('brands/', views.brands, name='brands'),
    path('brand/<slug:brand_slug>/', views.products_by_brand, name='products_by_brand'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)