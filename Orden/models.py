from django.db import models
from Inventario.models import Material

# Create your models here.

class Orden_Material(models.Model):
    codigo_orden = models.CharField(max_length=50,blank=False,null=True)
    material = models.ForeignKey(Material,null=True,blank=True,on_delete=models.CASCADE)
    fecha_termino = models.DateField()
    cantidad_material = models.IntegerField(default=0,blank=False,null=True)
