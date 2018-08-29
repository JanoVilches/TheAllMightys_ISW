from django.shortcuts import render, redirect
from Orden.forms import Ordenar_material_Form, Orden_Compra_Form
from Orden.models import Orden_Material, Orden_Compra
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from Orden.serializers import *

# Create your views here.

class OrdenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Orden_Material.objects.all()
    serializer_class = OrdenSerializer


def ordenar_material_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)

    if request.method == 'POST':
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

def estado_edit(request, id_orden):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)

    orden = Orden_Material.objects.get(id = id_orden)
    if request.method == 'GET':
        form = Ordenar_material_Form(instance=orden)
    else:
        form = Ordenar_material_Form(request.POST, instance=orden)
        if form.is_valid():
            form.save()
        return redirect('orden_materiales_list')
    return render(request, 'orden/solicitar_material.html', {'form':form})

def orden_compra_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)

    if request.method == 'POST':
        form = Orden_Compra_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('orden_compra_list')

    else:
        form = Orden_Compra_Form()

    return render(request, 'orden/solicitar_compra.html', {'form':form})

def ordenes_compra_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)

    orden_consult = Orden_Compra.objects.all()
    cont = {'ordenes_comp': orden_consult}
    return render(request, 'orden/ver_ordenes_compra.html', cont)
