from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from estudiantes.models import Estudiante, Clase


# vistas estudiantes
class ShowStudents(ListView):
    model = Estudiante
    context_object_name = 'estudiantes'


class DetailStudent(DetailView):
    model = Estudiante
    context_object_name = 'estudiante'


class CreateStudent(CreateView):
    model = Estudiante
    fields = '__all__'
    success_url = '/estudiantes/'


# vistas Clases
class ShowClasses(ListView):
    model = Clase
    context_object_name = 'clases'


class DetailClass(DetailView):
    model = Clase
    context_object_name = 'clase'

