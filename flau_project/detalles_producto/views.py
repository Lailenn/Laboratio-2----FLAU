from django.shortcuts import render

def index(request):
    return render(request, 'detalles_producto/index.html')
