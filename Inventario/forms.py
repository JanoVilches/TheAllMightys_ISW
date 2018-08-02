from django import forms
from Inventario.models import Material

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
