from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request,'recetas/index.html')


def base(request):
    return render(request, 'recetas/entradas.html')