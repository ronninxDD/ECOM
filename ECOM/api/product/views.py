from django.shortcuts import render

from .serializers import ProductSerializer
from .models import Products    
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all().order_by('name')
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
