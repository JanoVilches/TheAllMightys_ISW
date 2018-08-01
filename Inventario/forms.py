from django import forms
from Inventario.models import Material, Solicitar_Material

class Ingresar_material_Form(forms.ModelForm):

    class Meta:
        model =  Material

        fields = [
            'nombre_material',
            'codigo',
            'cantidad',
            'bodega',
        ]

        labels = {
            'nombre_material': 'Nombre Material',
            'codigo': 'Codigo Material',
            'cantidad': 'Cantidad del Material',
            'bodega': 'Bodegas'
        }

        widgets = {
            'nombre_material': forms.TextInput(attrs={'class':'form-control'}),
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad':forms.NumberInput(attrs={'class':'form-control'}),
            'bodega': forms.CheckboxSelectMultiple(),
        }

class Solicitar_material_Form(forms.ModelForm):

    class Meta:
        model =  Solicitar_Material

        fields = [
            'codigo_orden',
            'material',
            'fecha_termino',
            'cantidad_material',
        ]

        labels = {
            'codigo_orden': 'Codigo Material',
            'material': 'Nombre Material',
            'fecha_termino': 'Fecha Pedido',
            'cantidad_material': 'Cantidad'
        }

        widgets = {
            'codigo_orden': forms.TextInput(attrs={'class':'form-control'}),
            'material': forms.Select(attrs={'class':'form-control'}),
            'fecha_termino':forms.DateInput(attrs={'class':'form-control'}),
            'cantidad_material': forms.NumberInput(attrs={'class':'form-control'}),
        }
