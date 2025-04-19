from unittest.mock import patch
from rest_framework import routers

from api.category.models import Category
from .import views
from django.urls import path, include
router = routers.DefaultRouter()
router.register(r'', views.CategoryViewSet)
urlpatterns = [
    path('',include(router.urls))
]