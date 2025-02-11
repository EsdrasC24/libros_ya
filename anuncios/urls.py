from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_anuncio, name='crear_anuncio'),
    path('anuncio/<int:id>/', views.detalle_anuncio, name='detalle_anuncio'),  # Detalle del anuncio
    # Otras URLs...
]
