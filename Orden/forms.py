from django import forms
from Orden.models import Orden_Material

class Ordenar_material_Form(forms.ModelForm):

    class Meta:
        model =  Orden_Material

        fields = [
            'codigo_orden',
            'material',
            'fecha_termino',
            'cantidad_material',
        ]

        labels = {
            'codigo_orden': 'Codigo Orden',
            'material': 'Nombre Material',
            'fecha_termino': 'Fecha Pedido',
            'cantidad_material': 'Cantidad'
        }

        widgets = {
            'codigo_orden': forms.TextInput(attrs={'class':'form-control'}),
            'material': forms.Select(attrs={'class':'form-control'}),
            'fecha_termino':forms.DateTimeInput(attrs={'class':'form-control'}),
            'cantidad_material': forms.NumberInput(attrs={'class':'form-control'}),
        }
