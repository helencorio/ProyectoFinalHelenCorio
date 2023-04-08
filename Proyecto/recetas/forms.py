from dataclasses import field
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class EntradaFormulario(forms.Form):   
    nombre_receta= forms.CharField(max_length=30)
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


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label="Modificar E-mail")
    username = forms.CharField(label="Modificar Nombre de Usuario")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if not self.instance.check_password(password1):
            raise forms.ValidationError("Contraseña incorrecta")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
