from django.db import models

class Cliente(models.Model):
    rut = models.CharField(primary_key = True, max_length = 15, verbose_name = "Rut")
    nombre = models.CharField(max_length = 50, verbose_name = "Nombre")
    a_paterno = models.CharField(max_length = 50, verbose_name = "Apellido Paterno")
    a_materno = models.CharField(max_length = 50, verbose_name = "Apellido Materno")
    telefono = models.CharField(max_length = 15, verbose_name = "Teléfono")
    direccion = models.CharField(max_length = 50, verbose_name = "Dirección")
    correo_electronico = models.CharField(max_length = 50, verbose_name = "Correo Electrónico")


