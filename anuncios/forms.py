from django import forms
from .models import Anuncio

class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['titulo', 'autor', 'edicion', 'estado', 'precio', 'condiciones_intercambio', 'fecha_publicacion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicar estilos atractivos a todos los campos
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-3 rounded-lg border-2 border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all duration-200 outline-none placeholder-gray-400 text-gray-700 bg-white shadow-sm hover:border-blue-400',
                'placeholder': f'Ingrese su {field.label.lower()}'
            })