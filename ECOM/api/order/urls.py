from unittest.mock import patch
from rest_framework import routers

from api.order.models import Order
from .import views
from django.urls import path, include
router = routers.DefaultRouter()
router.register(r'', views.OrderViewSet)
urlpatterns = [
    path('add/<str:id>/<str:token>' , views.add , name='order.add'),
    path('',include(router.urls))
]