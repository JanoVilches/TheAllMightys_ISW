from django.contrib.auth.models import User
from django.views.generic import CreateView
from login.forms import CreateUserForm

class RegistroUsuario(CreateView):
    model = User
    template_name = "login/registrar.html"
    form_class = CreateUserForm
    success_message = "Usuario registrado"
    success_url = "http://127.0.0.1:8000/"

# Create your views here.
