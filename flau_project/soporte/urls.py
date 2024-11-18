from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='soporte'),
     path('soporte/', views.index, name='index'),
]
# urls.py en tu aplicación


