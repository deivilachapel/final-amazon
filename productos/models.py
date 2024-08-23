# Models.py

from django.db import models

# Create your models here.
class Producto(models.Model):
    TIPO_PRODUCTO_CHOICES = [
        ('local', 'Local'),
        ('internacional', 'Internacional'),
    ]

    codigo = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=15, choices=TIPO_PRODUCTO_CHOICES)
    imagen = models.ImageField(upload_to='productos/imagenes/', null=True, blank=True)

    def __str__(self):
        return self.descripcion