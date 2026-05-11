from django.shortcuts import render, redirect, get_object_or_404
from .models import Profesor
from .forms import ProfesorForm

# 1. READ (El que ya tienes)
def datos_profesor(request):
    profesores = Profesor.objects.all()
    return render(request, 'datosProfesor.html', {'profesores': profesores})

# 2. CREATE (Crear)
def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save() # Guarda en la base de datos
            return redirect('datos_profesor') # Te regresa a la lista
    else:
        form = ProfesorForm()
    return render(request, 'formulario_profesor.html', {'form': form})

# 3. UPDATE (Editar)
def editar_profesor(request, id):
    # Busca al profesor por su ID, si no existe lanza error 404
    profesor = get_object_or_404(Profesor, id=id)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('datos_profesor')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'formulario_profesor.html', {'form': form})

# 4. DELETE (Eliminar)
def eliminar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    if request.method == 'POST':
        profesor.delete()
        return redirect('datos_profesor')
    return render(request, 'confirmar_eliminacion.html', {'profesor': profesor})