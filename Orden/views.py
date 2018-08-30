from django.shortcuts import render, redirect
from Orden.forms import Ordenar_material_Form, Orden_Compra_Form
from Orden.models import Orden_Material, Orden_Compra
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

# Create your views here.

def ordenes_from_erp(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
        
    info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
    url, db, username, password = info['host'], info['database'], info['user'], info['password']
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    lista = models.execute_kw(db, uid, password,'account.invoice', 'search_read', [],{'fields': ['create_date', 'commercial_partner_id', 'amount_total','user_id','date_due'],'limit':5})
    #Ordenar lista a dicctionario
    dict = {'ordenes':lista}
    return render(request, 'orden/ordenes_erp.html', dict)

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
