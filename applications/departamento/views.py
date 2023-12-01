from django.shortcuts import render
from django.views.generic import *
from .forms import *
from applications.empleados.models import Empleado
from .models import Departamento

# Create your views here.

class DepartamentoListView(ListView):
    template_name = "departamento/listar_departamentos.html"
    model = Departamento
    context_object_name = 'departamentos'

class DepartamentoDetailView(DetailView):
    model = Departamento
    template_name = "departamento/detail.html"
    context_object_name = 'departamento'

class DepartamentoFormView(FormView):
    template_name = 'departamento/añadir.html'
    form_class = DepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print('*********Estamos en el form valid*********')
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['nombre_corto'],
            activo=True
        )
        depa.save()
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )

        return super(DepartamentoFormView, self).form_valid(form)