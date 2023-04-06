from django.shortcuts import render
from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse

# Modelos ---------------------------------------------------------------------------------
from recetas.models import Entrada, Platoprincipal, Postre, Vegano, Singluten

# Formularios -----------------------------------------------------------------------------
from recetas.forms import EntradaFormulario,  PlatoprincipalFormulario, UserRegisterForm, UserEditForm, PostreFormulario, VeganoFormulario,SinglutenFormulario

# INICIO Vistas basadas en Clases ----------------------------------------------------------
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# FIN Vistas basadas en clases --------------------------------------------------------------

# Importamos todo lo necesario para hacer autenticación ------------------------------------- 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Fin Autenticación -------------------------------------------------------------------------



# Create your views here.


def inicio(request):
    return render(request,'recetas/index.html')

def entrada(request):
    return render(request, 'recetas/entradas.html')

def platoprincipal(request):
    return render(request, 'recetas/platos_principales.html')

def postre(request):
    return render(request, 'recetas/postres.html')

def vegano(request):
    return render(request, 'recetas/veganos.html')

def singluten(request):
    return render(request, 'recetas/singluten.html')

def mostrar_entradas(request):
    return render(request, 'recetas/entradas_list.html')




def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario,password = contra)

            if user is not None:
                login(request,user)

                return render(request,"recetas/index.html",{"mensaje":f"Bienvenido {usuario}"})
            else:
                
                return render(request,"recetas/index.html",{"mensaje":"Error,datos incorrectos"})

        else:
            
                return render(request,"recetas/index.html",{"mensaje":"Error,formulario erroneo"})

    form = AuthenticationForm()

    return render(request,"recetas/login.html",{'form':form})



def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"recetas/index.html",{"mensaje":"Usuario Creado :)"})
    else:
        form = UserRegisterForm()
        #form = UserCreationForm()
    return render(request,"recetas/registro.html",{"form":form})



def inicio(request):
    return render(request,"recetas/index.html")

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1= informacion['password1']
            usuario.password2= informacion['password1']            
            usuario.save()
            

            return render(request, "recetas/index.html")
    else:

        miFormulario = UserEditForm(initial={'email':usuario.email})
    return render(request, "recetas/editarPerfil.html",{"miFormulario": miFormulario, "usuario":usuario})



#-----------------------------------------Avatar-------------------------------------------------------
#@login_required
#def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    #return render(request,"recetas/base.html", {"url":avatares[0].imagen.url})





def formularioEntrada(request):
    if request.method == 'POST':
        miFormulario = EntradaFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
	
            entrada= Entrada(
            nombre_receta=informacion['nombre_receta'],
            duracion=informacion['duracion'],
            ingredientes=informacion['ingredientes'],
            procedimiento=informacion['procedimiento'],)

            entrada.save()

            entradas = Entrada.objects.all()
    
            return render(request,"recetas/entradas.html",{"entradas":entradas})
