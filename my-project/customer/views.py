from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse('Hola mundo desde Inicio')

# Diccionario que mapea cada día de la semana a su frase
frase_dia = {
    'lunes': 'Hoy es lunes',
    'martes': 'Hoy es martes',
    'miercoles': 'Hoy es miercoles',
    'jueves': 'Hoy es jueves',
    'viernes': 'Hoy es viernes',
    'sabado': 'Hoy es sabado',
    'domingo': 'Hoy es domingo'
}

# 'dia' llega como parámetro dinámico desde la URL (ej: /lunes → dia='lunes')
def dia_semana(request, dia):
    texto_por_dia = frase_dia[dia]
    return HttpResponse(texto_por_dia)