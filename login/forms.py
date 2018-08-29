from django import forms
from django.contrib.auth.models import User
from login.models import Profile

Usuarios = (('1','Bodeguero'),('2','Encargado de Compras'),('3','Obrero'))

class CreateUserForm(forms.ModelForm):
    class Meta:
        model= User
        fields =['username','password','email']
        labels = {
            'username': 'Usuario',
            'password': 'Contraseña',
            'email': 'Correo'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'})
        }

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields =['tipo_usuario']
        labels = {
            'tipo_usuario': 'Tipo de Usuario'
        }
        widgets = {
            'tipo_usuario': forms.Select(attrs={'class':'form-control'},choices=Usuarios)
        }
