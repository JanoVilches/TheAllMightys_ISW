from django.conf.urls import url, include
from Inventario.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^crear$', Ingresar_material_view, name='Ingresar_material'),
    url(r'^listar$', materiales_list, name='ver_materiales'),
    url(r'^solicitar$', Solicitar_Material, name='solicitar_material'),

]
