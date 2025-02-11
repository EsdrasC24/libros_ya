from django.db import models
from django.utils import timezone

class Anuncio(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    edicion = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    condiciones_intercambio = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
