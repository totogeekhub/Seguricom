from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import ProfeForm,UserCreationFormWithEmail
from django import forms

class ProfeListView(ListView):
    model = User
    queryset = User.objects.filter(level = 1)
    template_name = 'profesional/profe_list.html'
    
    
class ProfeDetailView(DetailView):
    model = User
    template_name = 'profesional/profe_detail.html'




@method_decorator(staff_member_required,name='dispatch')
class ProfeCreate(CreateView):
    model = User
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('profesionales:profesionales')
    template_name = 'profesional/profe_form.html'


    def get_form(self, form_class=None):
        form = super(ProfeCreate, self).get_form()
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
class ProfeUpdate(UpdateView): 
    model = User
    form_class = ProfeForm
    template_name_suffix = '_update_form'
    template_name = 'profesional/profe_update_form.html'



    def get_success_url(self):
        return reverse_lazy('profesionales:profesionales')

@method_decorator(staff_member_required,name='dispatch')
class ProfeDelete(DeleteView):
    model = User
    success_url = reverse_lazy('profesionales:profesionales')
    template_name = 'profesional/profe_confirm_delete.html'


