from django.conf.urls import url, include
from Inventario.views import *

urlpatterns = [
    url(r'Home', index, name='index'),
    url(r'crear_material', Ingresar_material_view, name='Ingresar_material'),
    url(r'matlist', materiales_list, name='ver_materiales'),
]
