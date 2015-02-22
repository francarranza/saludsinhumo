from django.db import models

class Form(models.Model):
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    DNI = models.IntegerField(max_length=8)
    Telefono = models.IntegerField(max_length=11)
    email = models.EmailField(max_length=75)
    RazonSocial= models.CharField(max_length=100)
    Direccion = models.CharField(max_length=50)
    MotivoDenuncia = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=300)
    FechaInfraccion = models.DataField('date published')
    Hora = models.TimeField('time published')
    VinculacionDenunciate = models.CharField(max_length = 20)
