# views.py

from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer

class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer