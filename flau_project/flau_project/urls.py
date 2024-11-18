from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('productos/', include('productos.urls')),
    path('detalles/', include('detalles_producto.urls')),
    path('soporte/', include('soporte.urls')),
    path('tienda_app/', include('tienda_app.urls')),

]
