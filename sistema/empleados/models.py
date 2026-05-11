from django.db import models

class Domicilio(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    colonia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.calle} #{self.numero}, {self.ciudad}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    # Esta es la llave foránea que une ambas tablas:
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"