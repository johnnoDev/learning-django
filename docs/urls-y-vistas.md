# URLs y Vistas en Django

Guía basada en los temas 51–55 del curso de Fundamentos de Django.

---

## 51. ¿Qué es una URL y una Vista?

- **URL (Uniform Resource Locator):** es la dirección que el usuario escribe en el navegador. Django recibe esa dirección y decide qué código ejecutar.
- **Vista (View):** es una función (o clase) de Python que recibe una petición HTTP y devuelve una respuesta HTTP.

El flujo básico es:

```
Navegador → URL → urls.py → views.py → HttpResponse → Navegador
```

---

## 52. Creando nuestra primera URL y Vista

### Paso 1 — Crear la app

```bash
python manage.py startapp <nombre_app>
```

### Paso 2 — Registrar la app en `settings.py`

```python
# config/settings.py
INSTALLED_APPS = [
    ...
    '<nombre_app>',
]
```

### Paso 3 — Crear una vista en `views.py`

```python
# <nombre_app>/views.py
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Hola mundo desde Django")
```

### Paso 4 — Crear `urls.py` dentro de la app

```python
# <nombre_app>/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
]
```

### Paso 5 — Incluir las URLs de la app en el proyecto

```python
# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', include('<nombre_app>.urls')),
]
```

Ahora `http://127.0.0.1:8000/inicio/` responde con "Hola mundo desde Django".

---

## 53. Creando más URLs y Vistas

Se pueden agregar tantas rutas como se necesiten en el `urlpatterns` de la app.

```python
# <nombre_app>/views.py
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Página de inicio")

def acerca(request):
    return HttpResponse("Página acerca de nosotros")

def contacto(request):
    return HttpResponse("Página de contacto")
```

```python
# <nombre_app>/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',        views.inicio),
    path('acerca/', views.acerca),
    path('contacto/', views.contacto),
]
```

---

## 54. Rutas Dinámicas

Las rutas dinámicas permiten capturar un fragmento variable de la URL y pasarlo como argumento a la vista.

```python
# <nombre_app>/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<dia>', views.dia_semana),
]
```

```python
# <nombre_app>/views.py
from django.http import HttpResponse, HttpResponseNotFound

def dia_semana(request, dia):
    if dia == "lunes":
        return HttpResponse("Hola, desde el día Lunes")
    elif dia == "martes":
        return HttpResponse("Hola, desde el día Martes")
    else:
        return HttpResponseNotFound("Día incorrecto. No existe")
```

Ejemplo: `http://127.0.0.1:8000/message/lunes` devuelve `"Hola, desde el día Lunes"`.

---

## 55. Convertidores de Rutas

Django incluye convertidores que validan y convierten automáticamente el tipo del parámetro en la URL antes de pasarlo a la vista.

| Convertidor | Captura | Tipo Python |
|-------------|---------|-------------|
| `str`       | Cualquier texto sin `/` (por defecto) | `str` |
| `int`       | Número entero positivo | `int` |
| `slug`      | Letras, números, guiones y guiones bajos | `str` |
| `uuid`      | UUID con formato estándar | `UUID` |
| `path`      | Texto incluyendo `/` | `str` |

### Ejemplo con `int`

```python
# urls.py
urlpatterns = [
    path('producto/<int:id>', views.detalle_producto),
]
```

```python
# views.py
from django.http import HttpResponse

def detalle_producto(request, id):
    return HttpResponse(f"Mostrando producto con ID: {id}")
```

Si el usuario visita `/producto/abc`, Django devuelve **404** automáticamente porque `abc` no es un entero.

### Ejemplo con `slug`

```python
# urls.py
urlpatterns = [
    path('articulo/<slug:titulo>', views.ver_articulo),
]
```

```python
# views.py
def ver_articulo(request, titulo):
    return HttpResponse(f"Artículo: {titulo}")
```

---

## Resumen del flujo completo

```
config/urls.py
    └── include('<app>.urls')
            └── <app>/urls.py
                    └── path('<ruta>', views.<funcion>)
                                          └── devuelve HttpResponse
```

[← Volver al README principal](../README.md)
