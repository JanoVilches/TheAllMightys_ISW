from django.conf.urls import url, include
from login.views import RegistroUsuario

urlpatterns = [
    url(r'^registrar',RegistroUsuario.as_view(),name="registrar")

]
