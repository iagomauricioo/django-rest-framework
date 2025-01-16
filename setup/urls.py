from django.contrib import admin
from django.urls import include, path
from escola.views import EstudanteViewSet, CursoViewSet, ListaEstudantesMatriculados, ListaMatriculasEstudante, MatriculaViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('estudantes', EstudanteViewSet, basename='Estudantes')
routers.register('cursos', CursoViewSet, basename='Cursos')
routers.register('matriculas', MatriculaViewSet, basename='Matriculas') 

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(routers.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculasEstudante.as_view(), name='estudante_matriculas'),
    path('cursos/<int:pk>/matriculas/', ListaEstudantesMatriculados.as_view(), name='curso_matriculas'),
]
