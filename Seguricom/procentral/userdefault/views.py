from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import DefaForm, UserCreationFormWithEmail
from django import forms


class StaffRequiredMixin(object):
    """
        Este Mixin requerira que el usuario sea miembro del staff
        """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.level == 2 :
            return redirect(reverse_lazy('pages:pages'))







        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)



class DefaListView(StaffRequiredMixin,ListView):
    model = User
    queryset = User.objects.filter(level = 4)
    template_name = 'userdefault/defa_list.html'
    
    
class DefaDetailView(StaffRequiredMixin,DetailView):
    model = User
    queryset = User.objects.filter(level = 4)
    template_name = 'userdefault/defa_detail.html'





class DefaUpdate(StaffRequiredMixin,UpdateView): 
    model = User
    form_class = DefaForm
    template_name_suffix = '_update_form'
    template_name = 'userdefault/defa_update_form.html'

    def get_success_url(self):
        return reverse_lazy('udefaults:udefaults')



class DefaDelete(StaffRequiredMixin,DeleteView):
    model = User
    success_url = reverse_lazy('udefaults:udefaults')
    template_name = 'userdefault/defa_confirm_delete.html'






class DefaCreate(StaffRequiredMixin,CreateView):
    model = User
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('udefaults:udefaults')
    template_name = 'userdefault/defa_form.html'


    def get_form(self, form_class=None):
        form = super(DefaCreate, self).get_form()
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
