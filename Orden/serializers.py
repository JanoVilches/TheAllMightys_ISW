from Orden.models import *
from rest_framework import serializers

class OrdenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orden_Material
        fields = ('codigo_orden','material','fecha_termino','cantidad_material')
