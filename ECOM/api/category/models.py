from ast import mod
from django.db import models
from django.forms import CharField, DateTimeField

# Create your models here.
class Category(models.Model):
    name = models.CharField( max_length=50)
    description = models.CharField( max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering=("name",)
        verbose_name_plural = 'Categories'
