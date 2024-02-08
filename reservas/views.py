from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente
from .forms import ClienteForm


def inicio(request):
    return render (request, 'paginas/inicio.html')

def registro(request):
    formulario = ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('cliente')
    return render (request, 'usuarios/registro.html', {'formulario' : formulario})


def login(request):
    return render (request, 'usuarios/login.html')

def contacto(request):
    return render (request, 'paginas/contacto.html')

def habitaciones(request):
    return render (request, 'catalogo_habitaciones/habitaciones.html')

def reservas(request):
    return render (request, 'catalogo_habitaciones/mis_reservas.html')

def editar_registro(request):
    return render (request, 'usuarios/editar registro.html')



