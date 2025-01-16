from escola.models import Curso, Estudante
from escola.serializers import CursoSerializer, EstudanteSerializer

from rest_framework import viewsets

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

