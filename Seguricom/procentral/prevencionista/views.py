from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import PrevenForm,UserCreationFormWithEmail
from django import forms

class PrevenListView(ListView):
    model = User
    queryset = User.objects.filter(level = 0)

    
class PrevenDetailView(DetailView):
    model = User


@method_decorator(staff_member_required,name='dispatch')
class PrevenCreate(CreateView):
    model = User
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('prevencionistas:prevencionistas')

    def get_form(self, form_class=None):
        form = super(PrevenCreate, self).get_form()
        # Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Repite la contraseña'})

        return form

@method_decorator(staff_member_required,name='dispatch')
class PrevenUpdate(UpdateView): 
    model = User
    form_class = PrevenForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('prevencionistas:prevencionistas')

@method_decorator(staff_member_required,name='dispatch')
class PrevenDelete(DeleteView):
    model = User
    success_url = reverse_lazy('prevencionistas:prevencionistas')


