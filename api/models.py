from django.db import models

# Create your models here.
class Ingrediente(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Hamburguesa(models.Model):
    nombre = models.TextField()
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.URLField()
    ingredientes = models.ManyToManyField(Ingrediente, related_name='hamburguesas',blank=True)

    def __str__(self):
        return self.nombre
