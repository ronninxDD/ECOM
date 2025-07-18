from django.db import models
from api.user.models import CustomUser
from api.product.models import Products
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomUser ,on_delete=models.CASCADE , null=True) 
    product_names = models.CharField(max_length=1000)
    total_products = models.CharField(max_length = 1000 , default=0)
    transaction_id = models.CharField(max_length=150, default=0)
    total_amount = models.CharField(max_length=50 , default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.email if self.user else 'Unknown User'}"
    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = 'Orders'