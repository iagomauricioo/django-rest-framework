from django.contrib import admin
from django.urls import include, path
from escola.views import EstudanteViewSet, CursoViewSet
from rest_framework import routers

routers = routers.DefaultRouter()

routers.register('estudantes', EstudanteViewSet, basename='Estudantes')
routers.register('cursos', CursoViewSet, basename='Cursos')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(routers.urls))
]
