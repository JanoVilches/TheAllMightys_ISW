from django.conf.urls import url, include
from Orden.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'crear_orden_mate', ordenar_material_view, name='ordenar_material'),
    url(r'orden_material_list', ordenes_material_list, name='orden_materiales_list'),
    url(r'orden_compra_list', ordenes_compra_list, name='orden_compra_list'),
    url(r'crear_orden_compra', orden_compra_view, name='orden_compra'),
    url(r'ordenes_erp', ordenes_from_erp, name='orden_erp'),
    url(r'editar_orden/(?P<id_orden>\d+)/$', estado_edit, name='editar_estado'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
