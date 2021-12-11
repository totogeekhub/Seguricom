from django import forms
from django.db.models import fields
from django.forms import widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class DefaForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email','level','first_name','last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Nombre de Usuario'}),
            'first_name': forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Nombre'}),
            'last_name': forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Apellido'}),
            'email': forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Correo'}),
            'level': forms.NumberInput(attrs={'name':'level','class':'form-control','min':'0','max':'4' , 'placeholder':'nivel'}),
#            'is_staff': forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Titulo'}),
#           'is_active': forms.Textarea(attrs={'class':'form-control' ,'placeholder':''}),
        }
        labels = {
             'level':'Nivel','email':'','username':''
        }


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email 

