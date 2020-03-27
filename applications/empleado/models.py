from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField


# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
            verbose_name = 'Habilidad'
            verbose_name_plural = 'Habilidades de empleado'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad


class Empleado(models.Model):
    """Modelo para tabla empleado"""
    JOB_CHOICES = (
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','Otro')
    )
    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)
    full_name = models.CharField('Nombre Completo', max_length=160, blank=True)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    hoja_vida = RichTextField()
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['job']
        unique_together = ('first_name','last_name')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + ' ' + self.last_name
