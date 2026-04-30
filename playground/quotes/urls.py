from django.urls import path
from . import views

# Ruta dinamica
urlpatterns = [
    path('<dia>', views.dia_semana)
]