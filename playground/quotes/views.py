from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hola mundo desde la Vista de Quote")

# Creando mas Views como práctica
def lunes(request):
    return HttpResponse("Hola Lunes")

def martes(request):
    return HttpResponse("Hola Martes")

def miercoles(request):
    return HttpResponse("Hola Miercoles")
    