from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('<int:dia>', views.dia_semana_numero),
    path('<str:dia>', views.dia_semana)  # <dia> captura cualquier texto de la URL y lo pasa como parámetro a la vista

]
