from django.db import models

# Create your models here.

class CategoryLanguage(models.Model):
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language

class CategoryBox(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Direction(models.Model):
    direction = models.CharField(max_length=150, verbose_name="Направление")

    def __str__(self):
        return self.direction 

class Products(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, null=True)
    image = models.ImageField(upload_to='image/')
    price = models.FloatField(default=500)
    site_maker_name = models.CharField(max_length=150, null=True)
    site_maker=models.URLField(max_length=255, null=True)
    category = models.ForeignKey(CategoryBox, on_delete=models.CASCADE)
    language = models.ForeignKey(CategoryLanguage, on_delete=models.SET_NULL , null=True)
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL , null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True )
    url = models.URLField(max_length=150)

    def __str__(self):
        return self.name 


