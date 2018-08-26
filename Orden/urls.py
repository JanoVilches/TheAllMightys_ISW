from django.conf.urls import url, include
from Orden.views import *

urlpatterns = [
    url(r'crear_orden_mate', ordenar_material_view, name='ordenar_material'),
    url(r'orden_material_list', ordenes_material_list, name='orden_materiales_list'),
    url(r'orden_compra_list', ordenes_compra_list, name='orden_compra_list'),
    url(r'crear_orden_compra', orden_compra_view, name='orden_compra'),
    url(r'editar_orden/(?P<id_orden>\d+)/$', estado_edit, name='editar_estado'),
]
