from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

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

def dia_semana_numero(request, dia):
    dias = list(frase_dia.keys())  # ['lunes', 'martes', ...]
    if dia > len(dias):
        return HttpResponse('El día no existe')
    dia_rediccionar = dias[dia-1]  # dia=1 → índice 0 → 'lunes'
    # Redirige al navegador a la ruta con el nombre del día (ej: /lunes)
    return HttpResponseRedirect(f'/{dia_rediccionar}')


# 'dia' llega como parámetro dinámico desde la URL (ej: /lunes → dia='lunes')
def dia_semana(request, dia):
    texto_por_dia = frase_dia[dia]
    return HttpResponse(texto_por_dia)