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

def editar_anuncio(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)  # Obtener el anuncio o mostrar un error 404 si no existe

    if request.method == 'POST':
        form = AnuncioForm(request.POST, instance=anuncio)  # Pre-llenar el formulario con los datos actuales
        if form.is_valid():
            form.save()  # Guardar los cambios
            return redirect('detalle_anuncio', id=anuncio.id)  # Redirigir a la página de detalles del anuncio
    else:
        form = AnuncioForm(instance=anuncio)  # Mostrar el formulario pre-llenado

    return render(request, 'editar_anuncio.html', {'form': form, 'anuncio': anuncio})


def lista_anuncios(request):
    anuncios = Anuncio.objects.all().order_by('-fecha_publicacion')  # Ordenar por fecha más reciente
    return render(request, 'lista_anuncios.html', {'anuncios': anuncios})
