from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='lista_anuncio'),
    path('crear/', views.crear, name='crear_anuncio'),
    path('editar/<int:id>', views.editar, name='editar_anuncio'),
    path('<int:id>/', views.detalle, name='detalle_anuncio'),
    path('<int:anuncio_id>/calificar/<int:me_gusta>/', views.calificar_anuncio, name='calificar_anuncio'),
    # Otras URLs..
]
