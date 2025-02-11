from django.shortcuts import render, redirect
from .forms import AnuncioForm

def crear(request):
    if request.method == 'POST':
        form = AnuncioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_anuncios')  # Redirige a la lista de anuncios después de crear uno
    else:
        form = AnuncioForm()
    
    return render(request, 'crear_anuncio.html', {'form': form})


def detalle_anuncio(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)  # Obtener el anuncio o mostrar un error 404 si no existe
    return render(request, 'detalle_anuncio.html', {'anuncio': anuncio})
