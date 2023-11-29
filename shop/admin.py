from django.contrib import admin
from .models import *
from .forms import *
from django.utils.text import slugify

admin.site.site_header = "Адміністративна панель"
admin.site.site_title = "Адміністративна панель"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm

    """
    Clean the slug field.
    
    Returns:
        str: The cleaned slug value.
    """

    def clean_slug(self):
        # Автоматичне створення slug на основі імені, якщо не вказано
        slug = self.cleaned_data.get("slug")
        if not slug:
            slug = slugify(self.cleaned_data["name"])
        return slug

    """
    Get the prepopulated fields for the given request and object.

    Parameters:
        request (Request): The request object.
        obj (Any): The object being edited (optional).

    Returns:
        dict: A dictionary containing the prepopulated fields.
    """

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    def clean_slug(self):
        # Автоматичне створення slug на основі імені, якщо не вказано
        slug = self.cleaned_data.get("slug")
        if not slug:
            slug = slugify(self.cleaned_data["name"])
        return slug

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}

class StatusProductAdmin(admin.ModelAdmin):
    # Якщо потрібно змінити відображення полів у списку об'єктів
    list_display = ('status',)

# Реєстрація моделі та адміністративних налаштувань
admin.site.register(StatusProduct, StatusProductAdmin)

@admin.register(Brand)
class brandAdmin(admin.ModelAdmin):
    # Якщо потрібно змінити відображення полів у списку об'єктів
    list_display = ('name',)
    def clean_slug(self):        # Автоматичне створення slug на основі імені, якщо не вказано
        slug = self.cleaned_data.get("slug")
        if not slug:
            slug = slugify(self.cleaned_data["name"])
        return slug 
    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}
    
