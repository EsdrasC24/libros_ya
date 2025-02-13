from django.db import models
from django.contrib.auth.models import User
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

    
class Calificacion(models.Model):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, related_name='calificaciones')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    me_gusta = models.BooleanField(default=True)  # True para "Me gusta", False para "No me gusta"

    class Meta:
        unique_together = ('anuncio', 'usuario')  # Un usuario solo puede calificar una vez un anuncio

    def __str__(self):
        return f"{self.usuario.username} - {'Me gusta' if self.me_gusta else 'No me gusta'}"
