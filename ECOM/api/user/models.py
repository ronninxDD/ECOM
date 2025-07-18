from tkinter import N
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=255,default='Anonymous',null=True,blank=True)
    email = models.EmailField(unique=True, max_length=255)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    phone = models.CharField(max_length=15, null=True, blank=True)
    session_token = models.CharField(max_length=10, default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
