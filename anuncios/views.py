from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnuncioForm
from .models import Anuncio, Calificacion

def crear(request):
    if request.method == 'POST':
        form = AnuncioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_anuncios')  # Redirige a la lista de anuncios después de crear uno
    else:
        form = AnuncioForm()
    
    return render(request, 'anuncios/crear.html', {'form': form})

def detalle(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)
    calificaciones = anuncio.calificaciones.all()
    me_gustas = calificaciones.filter(me_gusta=True).count()
    no_me_gustas = calificaciones.filter(me_gusta=False).count()

    context = {
        'anuncio': anuncio,
        'me_gustas': me_gustas,
        'no_me_gustas': no_me_gustas,
    }
    return render(request, 'anuncios/detalle.html', context)

def calificar_anuncio(request, anuncio_id, me_gusta):
    anuncio = get_object_or_404(Anuncio, id=anuncio_id)
    usuario = request.user

    # Verificar si el usuario ya calificó este anuncio
    calificacion, creado = Calificacion.objects.get_or_create(
        anuncio=anuncio,
        usuario=usuario,
        defaults={'me_gusta': me_gusta}
    )

    if not creado:
        # Si ya existe, actualizar la calificación
        calificacion.me_gusta = me_gusta
        calificacion.save()

    return redirect('detalle_anuncio', id=anuncio.id)


def editar(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)
    
    if request.method == 'POST':
        form = AnuncioForm(request.POST, instance=anuncio)
        if form.is_valid():
            form.save()
            return redirect('detalle_anuncio', id=anuncio.id)
    else:
        form = AnuncioForm(instance=anuncio)
    
    return render(request, 'anuncios/editar.html', {'form': form, 'anuncio': anuncio})

def lista(request):
    anuncios = Anuncio.objects.all()  # Obtener todos los anuncios
    return render(request, 'anuncios/lista.html', {'anuncios': anuncios})