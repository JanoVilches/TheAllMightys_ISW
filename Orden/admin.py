from __future__ import unicode_literals
from django.contrib import admin
from .models import Orden_Material, Orden_Compra

admin.site.register(Orden_Material)
admin.site.register(Orden_Compra)
