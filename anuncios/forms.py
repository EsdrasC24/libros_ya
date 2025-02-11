from django import forms
from .models import Anuncio

class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['titulo', 'autor', 'edicion', 'estado', 'precio', 'condiciones_intercambio', 'fecha_publicacion']
