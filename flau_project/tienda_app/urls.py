# tienda/tienda_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tienda_app'),
]
