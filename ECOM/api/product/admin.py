from django.contrib import admin
from .models import Products
from django.utils.html import format_html
# Register your models here.

admin.site.register(Products)
