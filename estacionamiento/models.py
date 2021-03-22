from django.db import models
from django.utils.timezone import now, localtime

from usuario.models import Persona

class Proveedor(models.Model):
    idProveedor = models.CharField(max_length=30, verbose_name='idProveedor')
    nombre_proveedor = models.CharField(max_length=30, verbose_name='Proveedor')

class RegistroEstacionamiento(models.Model):
    tipo = models.CharField(max_length=30, verbose_name='Tipo')
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, verbose_name='Persona',null=True,blank=True)
    noSocio = models.IntegerField(blank=True ,null=True, verbose_name='DNI')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name='Proveedor',null=True,blank=True)
    lugar = models.CharField(max_length=30, verbose_name='Lugar')
    tiempo = models.DateTimeField(default=now, verbose_name='Fecha y Hora')
    direccion = models.CharField(max_length=30, default='ENTRADA', verbose_name='Dirección')
    autorizado = models.BooleanField(default=False, verbose_name='Autorización')
    cicloCaja = models.IntegerField(null=True, verbose_name='cicloCaja')
    cicloMensual = models.IntegerField(null=True, verbose_name='cicloMensual')
    identificador = models.CharField(max_length=30, verbose_name='Identificador', default = "Error")

    def __str__(self):
        if self.tipo == "SOCIO" or self.tipo == "SOCIO-MOROSO" :
            return str(localtime(self.tiempo)) + " - " + str(self.persona)
        elif self.tipo == "NOSOCIO":
            return str(localtime(self.tiempo)) + " - " + str(self.noSocio)
        elif self.tipo == "PROVEEDOR":
            return str(localtime(self.tiempo)) + " - " + str(self.proveedor)
        else:
            return "Error Fatal"


class Cobros(models.Model):
    precio = models.FloatField(verbose_name='precio')
    registroEstacionamiento = models.ForeignKey(RegistroEstacionamiento, on_delete=models.CASCADE, verbose_name='registroEstacionamiento')

class CicloCaja(models.Model):
    cicloCaja = models.IntegerField(verbose_name='cicloCaja')

class CicloMensual(models.Model):
    cicloMensual = models.IntegerField(verbose_name='cicloMensual')