from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_estudiantes, name='lista_estudiantes'),
    path('crear/', views.crear_estudiante, name='crear_estudiante'),
    path('<int:id>/', views.detalle_estudiante, name='detalle_estudiante'),
    path('<int:id>/editar/', views.editar_estudiante, name='editar_estudiante'),
    path('<int:id>/eliminar/', views.eliminar_estudiante, name='eliminar_estudiante'),
]
