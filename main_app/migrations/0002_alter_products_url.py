# Generated by Django 4.1.7 on 2023-02-21 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='url',
            field=models.SlugField(max_length=150),
        ),
    ]
