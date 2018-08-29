from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from Inventario.forms import Ingresar_material_Form
from Inventario.models import Material

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)

    return render(request, 'inventario/index.html')

def Ingresar_material_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)

    if request.method == 'POST':
        form = Ingresar_material_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ver_materiales')

    else:
        form = Ingresar_material_Form()

    return render(request, 'inventario/agregar_material.html', {'form':form})

def materiales_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)

    materiales_consult = Material.objects.all().order_by('id')
    contexto = {'materiales': materiales_consult}
    return render(request, 'inventario/ver_materiales.html', contexto)

def material_edit(request, id_material):
    material = Material.objects.get(id = id_material)
    if request.method == 'GET':
        form = Ingresar_material_Form(instance=material)
    else:
        form = Ingresar_material_Form(request.POST, instance=material)
        if form.is_valid():
            form.save()
        return redirect('ver_materiales')
    return render(request, 'inventario/agregar_material.html', {'form':form})

def material_delete(request, id_material):
    material = Material.objects.get(id = id_material)
    if request.method == 'POST':
        material.delete()
        return redirect('ver_materiales')
    return render(request, 'inventario/material_delete.html', {'material':material})
