"""
URL configuration for libros_ya project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from credenciales import views as credenciales_views
from anuncios import views as anuncios_views

urlpatterns = [
    path('', credenciales_views.iniciar_sesion, name='iniciar_sesion'),
    path('inicio', anuncios_views.inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('cerrar-sesion/', auth_views.LogoutView.as_view(), name='cerrar_sesion'),
    path('registro/', credenciales_views.registrar, name='registro'),
    path('anuncios/', include('anuncios.urls'))
]
