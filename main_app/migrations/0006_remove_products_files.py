# Generated by Django 4.1.7 on 2023-02-22 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_products_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='files',
        ),
    ]
