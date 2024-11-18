# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Soporte  # Asegúrate de tener el modelo Soporte configurado en models.py

def index(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')
        
        # Guardar en la base de datos
        soporte = Soporte(
            nombre=nombre,
            correo=correo,
            telefono=telefono,
            asunto=asunto,
            mensaje=mensaje
        )
        soporte.save()

        # Mensaje de éxito
        messages.success(request, 'Tu solicitud ha sido enviada correctamente.')
        
        # Redireccionar a la misma página o a una página de confirmación
        return redirect('index')

    # Renderizar el formulario en caso de GET
    return render(request, 'soporte/index.html')
