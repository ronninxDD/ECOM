from django.db import models
from api.category.models import Category
# Create your models here.
class Products (models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)  
    price = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True, related_name='products')
    def __str__(self):
        return self.name 
    class Meta:
        ordering=("name",)
        verbose_name_plural = 'Products'