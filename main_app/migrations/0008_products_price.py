# Generated by Django 4.1.7 on 2023-02-24 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_direction_products_direction'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.FloatField(default=500),
        ),
    ]