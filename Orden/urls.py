from django.conf.urls import url, include
from Orden.views import *

urlpatterns = [
    url(r'crear_orden_mate', ordenar_material_view, name='ordenar_material'),
    url(r'ordmatlist', ordenes_material_list, name='orden_material_list'),
]
