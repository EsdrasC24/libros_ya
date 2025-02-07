from django.db import models
from django.contrib.auth.models import User

from horarios.models import Horario

# Create your models here.

class Estudiante(models.Model):
#    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    horarios = models.ManyToManyField(Horario)

    def __str__(self):
        return self.usuario.username
