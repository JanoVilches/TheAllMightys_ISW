from django.conf.urls import url, include
from Orden.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'crear_orden_mate', ordenar_material_view, name='ordenar_material'),
    url(r'orden_material_list',ordenes_material_list, name='orden_materiales_list'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
