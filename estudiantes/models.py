from django.db import models


# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100 ,default="")
    apellido = models.CharField(max_length=200, default="")
    direccion = models.CharField(max_length=250, default="")
    matricula = models.IntegerField(null=True, default=None)
    activo = models.BooleanField(default=False)
    semestre = models.CharField(max_length=50, default="")
    foto = models.ImageField(blank=True, upload_to='media')

    def __str__(self):
        return self.nombre


class Clase(models.Model):
    materia = models.CharField(max_length=100, default="")
    semestre = models.CharField(max_length=100, default="")
    formacion = models.CharField(max_length=100, default="")
    estudiantes = models.ManyToManyField(Estudiante, related_name="clase")

    def __str__(self):
        return self.materia


