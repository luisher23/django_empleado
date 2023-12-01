from django.db import models
from applications.departamento.models import Departamento

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleados'
        ordering = ['id']

    def __str__(self):
        return f"{self.habilidad}"

class Empleado(models.Model):
    # Modelo para tabla empleado

    JOB_CHOICES = [
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    ]
    
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name='Departamento')
    full_name = models.CharField('Nombre completo', max_length=120, blank=True)
    avatar = models.ImageField('Avatar', upload_to='empleado', blank=True, null=True)
    habilidad = models.ManyToManyField(Habilidades, verbose_name='Habilidades')

    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['id']


    def __str__(self):
        return f"{self.id} | Nombre: {self.first_name} {self.last_name} | Departamento:  {self.departamento}"