from django.contrib import admin
from django.urls import path
from empleados.views import datos_profesor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profesores/', datos_profesor, name='datos_profesor'),
]