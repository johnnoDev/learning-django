from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# Crear una vista para una ruta dinamica

def dia_semana(request, dia):
    texto = None
    if dia == "lunes":
        texto = "Hola, desde el día Lunes"
    elif dia == "martes":
        texto = "Hola, desde el día martes"
    else:
        return HttpResponseNotFound("Día incorrecto. No existe")
    
    return HttpResponse(texto)