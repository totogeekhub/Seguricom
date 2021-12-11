

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.regex_helper import NonCapture
from actividad.models import ActividadSoli,Tipoactividad

from .models import Solicitud




class SoliForm(forms.ModelForm,):
    


    class Meta:
        model = Solicitud
        fields = ['respuesta','descrip','tipo_solicitud','usuario_solicitante']
        widgets = {
            'descrip': forms.Textarea(attrs={'class':'form-control', 'disabled':'disabled','placeholder':'Describa lo que necesita?, y cuando lo necesita?'}),
            'tipo_solicitud': forms.Select(attrs={'name':'tipo_act', 'id':'id_tipo_act','class':'form-control' ,'placeholder':'Que necesita?'}),
            'respuesta': forms.TextInput(attrs={'class':'form-control'})
            
        }
        
        labels = {
             'descrip':'','tipo_solicitud':'Que es lo que desea Solicitar' ,'respuesta':'Respuesta'
        }
        
        




