from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

admin.site.site_header = "Administración de la Aplicación de Empleados"
admin.site.site_title = "Panel de Administracion | App"

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'nombre_completo'
    )

    # Funcion full_name

    def nombre_completo(self, obj):
        print(obj)
        return obj.first_name + ' ' + obj.last_name


    search_fields = ('first_name',)
    list_filter = ('job', 'habilidad', 'departamento')
    filter_horizontal = ('habilidad',)

    
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)
