from django.urls import path
from .views import *


app_name = "empleados_app"

urlpatterns = [
    path('', InicioView.as_view(), name="inicio"),
    path('listar_empleados/', ListarEmpleados.as_view(), name="listar_empleados"),
    path('listar_area/<name>', ListarPorArea.as_view(), name="empleados_area"),
    path('listar_empleados_admin/', ListarEmpleadosAdmin.as_view(), name="listar_empleados_admin"),
    path('buscar_empleado/', ListarEmpleadosPorPalabraClave.as_view(),name="buscar_empleado"),
    path('listar_habilidades/<int:id>', ListarHabilidadesEmpleado.as_view()),
    path('detalle_empleado/<pk>', EmpleadoDetailView.as_view(), name="detalle_empleado"),
    path('crear_empleado/', EmpleadoCreateView.as_view(), name="crear_empleado"),
    path('success/', SuccessView.as_view(), name="correcto"),
    path('actualizar_empleado/<pk>', EmpleadoUpdateView.as_view(), name="actualizar_empleado"),
    path('eliminar_empleado/<pk>', EmpleadoDeleteView.as_view(), name="eliminar_empleado")
]
