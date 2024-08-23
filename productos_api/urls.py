# urls.py

from django.contrib import admin
from django.urls import path
from productos.views import ProductoListCreate, ProductoCreateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta URL permitirá tanto listar como crear productos
    path('api/productos/', ProductoListCreate.as_view(), name='producto-list-create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)