# Generated by Django 4.2.7 on 2023-11-25 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_brands_img'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='brands',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='brands',
            new_name='brand',
        ),
    ]
