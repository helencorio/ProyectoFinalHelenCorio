from django.shortcuts import render
from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse

# Modelos ---------------------------------------------------------------------------------
from recetas.models import Entrada, Platoprincipal, Postre, Vegano, Singluten

# Formularios -----------------------------------------------------------------------------
from recetas.forms import EntradaFormulario,  PlatoprincipalFormulario, UserRegisterForm, PostreFormulario, VeganoFormulario,SinglutenFormulario

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

def login(request):
    return render(request, 'recetas/login.html')

