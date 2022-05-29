from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class miembros(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(blank=True, null=True)
    fecha_nac = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)

