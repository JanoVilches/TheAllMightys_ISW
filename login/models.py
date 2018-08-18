from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=50,blank=False,null=True)
    password = models.CharField(max_length=30,blank=False,null=True)
    tipo_usuario = models.IntegerField(default=0,blank=False,null=False)

    def __str__(self):
        return '{}'.format(self.nombre_usuario)
