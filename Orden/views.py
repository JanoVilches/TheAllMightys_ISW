from django.shortcuts import render, redirect
from Orden.forms import Ordenar_material_Form
from Orden.models import Orden_Material
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from Orden.serializers import *

# Create your views here.

def ordenar_material_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)

    if not request.method == 'POST':
        form = Ordenar_material_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('orden_materiales_list')

    else:
        form = Ordenar_material_Form()

    return render(request, 'orden/solicitar_material.html', {'form':form})

def ordenes_material_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)

    orden_consult = Orden_Material.objects.all()
    cont = {'ordenes_mat': orden_consult}
    return render(request, 'orden/ver_ordenes_materiales.html', cont)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Orden_Material.objects.all().order_by('fecha_termino')
    serializer_class = OrdenSerializer
