from django.db import models
from datetime import datetime


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Blog(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank= True)
    photo = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
