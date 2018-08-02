from django.db import models

# Create your models here.

class Bodega(models.Model):
    nombre_bodega = models.CharField(max_length=200,blank=False,null=True)
    direccion = models.CharField(max_length=200,blank=False,null=True)

    def __str__(self):
        return '{}'.format(self.nombre_bodega)


class Material(models.Model):
    nombre_material = models.CharField(max_length=50,blank=False,null=True)
    codigo = models.CharField(max_length=30,blank=False,null=True)
    cantidad = models.IntegerField(default=0,blank=False,null=False)
    bodega = models.ManyToManyField(Bodega,blank=True)

    def __str__(self):
        return '{}'.format(self.nombre_material)
