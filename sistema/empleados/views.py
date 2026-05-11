from django.shortcuts import render
from .models import Profesor

def datos_profesor(request):
    # Esto obtiene todos los profesores (y sus domicilios atados por la Foreign Key)
    profesores = Profesor.objects.all()
    return render(request, 'datosProfesor.html', {'profesores': profesores})