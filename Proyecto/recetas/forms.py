from dataclasses import fields
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class EntradaFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    duracion= forms.IntegerField()
    ingredientes= forms.CharField(max_length=60)
    procedimiento= forms.CharField(max_length=500)
    
class PlatoprincipalFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    duracion= forms.IntegerField()
    ingredientes= forms.CharField(max_length=60)
    procedimiento= forms.CharField(max_length=500)

class PostreFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    duracion= forms.IntegerField()
    ingredientes= forms.CharField(max_length=60)
    procedimiento= forms.CharField(max_length=500)

class VeganoFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    duracion= forms.IntegerField()
    ingredientes= forms.CharField(max_length=60)
    procedimiento= forms.CharField(max_length=500)

class SinglutenFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    duracion= forms.IntegerField()
    ingredientes= forms.CharField(max_length=60)
    procedimiento= forms.CharField(max_length=500)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar E-mail")
    password1= forms.CharField(label='Contraseña Antigua', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la contraseña Antigua', widget=forms.PasswordInput)

    
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}        