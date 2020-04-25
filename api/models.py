from django.db import models

# Create your models here.
class Ingrediente(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()


class Hamburguesa(models.Model):
    nombre = models.TextField()
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.URLField()
    ingredientes = models.ManyToManyField(Ingrediente)
