from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_anuncios, name='lista_anuncios'),  # Página principal
    path('crear/', views.crear_anuncio, name='crear_anuncio'),
    path('anuncio/<int:id>/', views.detalle_anuncio, name='detalle_anuncio'),  # Detalle del anuncio
    path('anuncio/editar/<int:id>/', views.editar_anuncio, name='editar_anuncio'),  # Editar anuncio
    # Otras URLs...
]
