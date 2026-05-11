from django.contrib import admin
from django.urls import path
from empleados.views import datos_profesor, crear_profesor, editar_profesor, eliminar_profesor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profesores/', datos_profesor, name='datos_profesor'),

    # Nuevas rutas CRUD:
    path('profesores/crear/', crear_profesor, name='crear_profesor'),
    path('profesores/editar/<int:id>/', editar_profesor, name='editar_profesor'),
    path('profesores/eliminar/<int:id>/', eliminar_profesor, name='eliminar_profesor'),
]
