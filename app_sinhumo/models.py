from django.db import models
from PIL import Image
from django.conf import settings

class Denuncia(models.Model):

    ide = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.PositiveIntegerField(max_length=8)
    telefono = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    denunciado = models.CharField(max_length=100)
    rubro = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    provincia = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='.', blank=True, null=True)

    def __unicode__(self):
        return self.nombre
