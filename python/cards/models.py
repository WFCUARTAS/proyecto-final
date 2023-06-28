from django.db import models

# Create your models here.
class Exclusivas(models.Model):
    titulo = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    precio_full = models.IntegerField()
    precio_descuento = models.IntegerField()
    calificacion = models.DecimalField(max_digits=3, decimal_places=2)
    imagen_url = models.CharField(max_length=200)


class Mejores(models.Model):
    destino = models.CharField(max_length=200)
    duracion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=3, decimal_places=2)
    calificacion = models.DecimalField(max_digits=3, decimal_places=2)
    imagen_url = models.CharField(max_length=200)

class Blogs(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen_url = models.CharField(max_length=200)