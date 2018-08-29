from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from login.forms import CreateUserForm, CreateProfileForm
from login.models import Profile

class RegistroUsuario(CreateView):
    template_name = "login/registrar.html"
    model = Profile
    form_class = CreateUserForm
    second_form_class = CreateProfileForm
    success_url = "http://127.0.0.1:8000/"

    def get_context_data(self, **kwargs):
        context = super(RegistroUsuario,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            self.object = self.get_object
            form = self.form_class(request.POST)
            form2 = self.second_form_class(request.POST)
            if form.is_valid() and form2.is_valid():
                user = form.save()
                user.profile.tipo_usuario = form2.cleaned_data.get('tipo_usuario')
                user.profile.save()
                return HttpResponseRedirect(self.get_success_url())
        else:
            form=form_class()
            form2=second_form_class()
        return render(request,'login/registrar.html',{'form':form,'form2':form2})
