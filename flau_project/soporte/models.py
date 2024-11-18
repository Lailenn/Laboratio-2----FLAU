from django.db import models

class Soporte(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    
    def __str__(self):
        return f"Soporte de {self.nombre}"

