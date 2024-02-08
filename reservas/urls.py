from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('usuarios/registro', views.registro, name='registro'),
    path('usuarios/login', views.login, name='login'),
    path('catalogo_habitaciones/habitaciones', views.habitaciones, name='habitaciones'),
    path('catalogo_habitaciones/mis_reservas', views.reservas, name='reservas'),
    path('paginas/contacto', views.contacto, name='contacto'),
    path('usuarios/editar_registro', views.editar_registro, name='editar'),
] 
