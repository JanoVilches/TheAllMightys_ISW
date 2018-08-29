from django import forms
from Orden.models import Orden_Material, Orden_Compra

class Ordenar_material_Form(forms.ModelForm):

    class Meta:
        model =  Orden_Material

        fields = [
            'codigo_orden',
            'material',
            'fecha_termino',
            'cantidad_material',
            'estado'
        ]

        labels = {
            'codigo_orden': 'Codigo Orden',
            'material': 'Nombre Material',
            'fecha_termino': 'Fecha Pedido',
            'cantidad_material': 'Cantidad',
            'estado': 'Estado'
        }

        widgets = {
            'codigo_orden': forms.TextInput(attrs={'class':'form-control'}),
            'material': forms.Select(attrs={'class':'form-control'}),
            'fecha_termino':forms.DateInput(attrs={'class':'form-control'}),
            'cantidad_material': forms.NumberInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
        }

class Orden_Compra_Form(forms.ModelForm):

    class Meta:
        model =  Orden_Compra

        fields = [
            'codigo_compra',
            'material',
            'cantidad_material',
        ]

        labels = {
            'codigo_orden': 'Codigo Orden',
            'material': 'Nombre Material',
            'cantidad_material': 'Cantidad'
        }

        widgets = {
            'codigo_orden': forms.TextInput(attrs={'class':'form-control'}),
            'material': forms.Select(attrs={'class':'form-control'}),
            'cantidad_material': forms.NumberInput(attrs={'class':'form-control'}),
        }
