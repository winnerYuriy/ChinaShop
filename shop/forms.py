from django import forms
from django.utils.text import slugify
from .models import *


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def clean_slug(self):
        # Автоматичне створення slug на основі імені, якщо не вказано
        slug = self.cleaned_data.get('slug')
        if not slug:
            slug = slugify(self.cleaned_data['name'])
        return slug

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_slug(self):
        # Автоматичне створення slug на основі імені, якщо не вказано
        slug = self.cleaned_data.get('slug')
        if not slug:
            slug = slugify(self.cleaned_data['name'])
        return slug


class ProductSearchForm(forms.Form):
    query = forms.CharField(label='Пошук товару', max_length=100)


class status_product(forms.ModelForm):
    status = forms.CharField(max_length=25, label='Статус')
    class Meta:
        model = StatusProduct
        fields = '__all__'  


class brandAdminForm(forms.ModelForm):
    brand = forms.CharField(max_length=100, label='Назва бренду')

    class Meta:
        model = Brand
        fields = '__all__'
