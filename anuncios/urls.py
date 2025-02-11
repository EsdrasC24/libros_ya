from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_anuncio, name='crear_anuncio'),
    # Otras URLs...
]
