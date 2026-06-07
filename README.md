# Django - Comandos Básicos

Referencia rápida de los comandos más usados en Django.

---

## Instalación

```bash
# Instalar Django en el entorno virtual
pip install django

# Verificar la versión instalada
pip show django
```

---

## Crear un Proyecto

```bash
# Forma estándar (crea carpeta con el nombre dado)
django-admin startproject <nombre_proyecto>

# Forma recomendada (usa "config" como carpeta de configuración en el directorio actual)
django-admin startproject config .
```

---

## Servidor de Desarrollo

```bash
# Iniciar el servidor (por defecto en http://127.0.0.1:8000/)
python manage.py runserver

# Iniciar en un puerto específico
python manage.py runserver 8080
```

---

## Aplicaciones (Apps)

```bash
# Crear una nueva app dentro del proyecto
python manage.py startapp <nombre_app>
```

---

## Base de Datos y Migraciones

```bash
# Crear archivos de migración a partir de los modelos
python manage.py makemigrations

# Aplicar las migraciones a la base de datos
python manage.py migrate

# Ver el estado de las migraciones
python manage.py showmigrations
```

---

## Superusuario (Admin)

```bash
# Crear un superusuario para el panel de administración
python manage.py createsuperuser
```

---

## Shell de Django

```bash
# Abrir la consola interactiva de Django
python manage.py shell
```

---

## Otros Comandos Útiles

```bash
# Ver todos los comandos disponibles
python manage.py help

# Verificar si el proyecto tiene errores
python manage.py check

# Limpiar sesiones expiradas de la base de datos
python manage.py clearsessions
```

---

## Documentación complementaria

- [URLs y Vistas en Django](./docs/urls-y-vistas.md)
