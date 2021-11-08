from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from estudiantes.models import Estudiante, Clase
from rest_framework.viewsets import ModelViewSet

from estudiantes.serializer import StudentSerializer, SubjectSerializer


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


# vistas Materias
class ShowClasses(ListView):
    model = Clase
    context_object_name = 'clases'


class DetailClass(DetailView):
    model = Clase
    context_object_name = 'clase'


# vistas REST
class StudentViewSet(ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = StudentSerializer


class SubjectViewSet(ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = SubjectSerializer
