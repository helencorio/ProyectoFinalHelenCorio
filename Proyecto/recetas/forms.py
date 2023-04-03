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
    
    # email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repita la contraseña', widget=forms.PasswordInput)