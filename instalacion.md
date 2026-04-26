# 1. Para instalar globalmente en Windows:
python -m pip install django

## Acceder al shell de django
django-admin shell

## 2. Crear un entorno virtual y después instalar django
python -m ven venv
venv\Scripts\activate
pip install django

## Crear un archivo donde contenga los paquetes instalados con su respectivia versión
pip freeze > requirements.txt