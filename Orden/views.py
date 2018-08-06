from django.shortcuts import render, redirect
from Orden.forms import Ordenar_material_Form
from Orden.models import Orden_Material

# Create your views here.

def ordenar_material_view(request):
    if request.method == 'POST':
        form = Ordenar_material_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('orden_materiales_list')

    else:
        form = Ordenar_material_Form()

    return render(request, 'orden/solicitar_material.html', {'form':form})

def ordenes_material_list(request):
    orden_consult = Orden_Material.objects.all()
    cont = {'ordenes_mat': orden_consult}
    return render(request, 'orden/ver_ordenes_materiales.html', cont)
