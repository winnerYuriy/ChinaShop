from django.db import models
from django.utils.text import slugify


class StatusProduct(models.Model):
    status = models.CharField(max_length=50, verbose_name='Статус', blank=True, null=True, default='')
    choises = (
        ('', 'звичайний'),
        ('акція', 'акція'),
        ('хіт продаж', 'хіт продаж'),
        ('новинка', 'новинка'),
    )
    
    def __str__(self):
        return self.status
    
    class Meta:
            verbose_name_plural = 'Статуси продуктів'
            verbose_name = 'Статус продукту'
            ordering = ['status']


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва бренду')
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    image = models.FileField(verbose_name='Фото бренду', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Бренди'
        verbose_name = 'Бренд'
        ordering = ['name']

class Category(models.Model):
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    image = models.FileField(verbose_name='Фото категорії')
    name = models.CharField(max_length=50, verbose_name='Назва')
    slug = models.SlugField(max_length=50, unique=True, editable=True, verbose_name='Посилання')
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Перетворення символів на великі, якщо категорія не має батьківської категорії
        if not self.parent_category:
            self.name = self.name.upper() 
        
        # Автоматичне створення slug на основі імені, якщо не вказано
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def clean_slug(self):  # Автоматичне створення slug на основі імені, якщо не вказано
        slug = self.cleaned_data.get('slug')
        if not slug:
            slug = slugify(self.cleaned_data['name'])
        return slug
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    def get_all_children(self):
        children = Category.objects.filter(parent_category=self)
        return children

    class Meta:
        verbose_name_plural = 'Категорії'
        verbose_name = 'Категорія'
        ordering = ['name']


class Product (models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія')
    buying_date = models.DateField(verbose_name='Дата покупки')
    image = models.FileField(verbose_name='Фото продукту')
    name = models.CharField(max_length=150, verbose_name='Назва')
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    seller_rating = models.FloatField(verbose_name='Рейтинг продавця') # seller_rating
    link = models.URLField(blank=True, null=True, verbose_name='Посилання на продукт в Китаї')
    buying_price = models.FloatField(verbose_name='Ціна покупки')
    description = models.CharField(max_length=255, verbose_name='Короткий опис') # description = models.TextField(verbose_name='Опис')
    full_description = models.TextField(verbose_name='Повний опис', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна', null=True, blank=True) # price = models.FloatField(verbose_name='Ціна продажу')
    count = models.IntegerField(verbose_name='Кількість')
    status = models.ForeignKey(StatusProduct, on_delete=models.CASCADE, verbose_name='Статус продукту', null=True, blank=True, default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Бренд', null=True, blank=True)

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def __str__(self):
        return self.name
      
    class Meta:
        verbose_name_plural = 'Продукти'
        verbose_name = 'Продукт'
        ordering = ['name']

    def save(self, *args, **kwargs):
        # Автоматичне створення slug на основі імені, якщо не вказано
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)






