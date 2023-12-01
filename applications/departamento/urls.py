from django.urls import path
from .views import *


app_name = "departamento_app"

urlpatterns = [
    path('añadir/', DepartamentoFormView.as_view(), name="añadir_departamento"),
    path('listar_departamento/', DepartamentoListView.as_view(), name="listar_departamentos"),
]
