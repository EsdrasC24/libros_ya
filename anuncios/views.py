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
