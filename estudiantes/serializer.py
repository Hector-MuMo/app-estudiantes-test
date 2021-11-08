from rest_framework.serializers import ModelSerializer
from estudiantes.models import Estudiante, Clase


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'
