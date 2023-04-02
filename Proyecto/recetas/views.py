from django.shortcuts import render



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
    return render(request, 'recetas/mostrarentradas.html')

