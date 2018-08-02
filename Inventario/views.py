from django.shortcuts import render, redirect
from django.http import HttpResponse
from Inventario.forms import Ingresar_material_Form
from Inventario.models import Material

# Create your views here.

def index(request):
    return render(request, 'inventario/index.html')

def Ingresar_material_view(request):
    if request.method == 'POST':
        form = Ingresar_material_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ver_materiales')

    else:
        form = Ingresar_material_Form()

    return render(request, 'inventario/agregar_material.html', {'form':form})

def materiales_list(request):
    materiales_consult = Material.objects.all()
    contexto = {'materiales': materiales_consult}
    return render(request, 'inventario/ver_materiales.html', contexto)
