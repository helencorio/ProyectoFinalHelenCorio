from django.shortcuts import render
from django.http import HttpResponse
from recetas.forms import EntradaFormulario,UserRegisterForm,UserEditForm, PlatoprincipalFormulario
from recetas.models import Entrada, Platoprincipal
#CVB
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
#--------------------------Login------------------------------------
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.
#--------------------------------------Entradas--------------------------------------

def entrada(request):
    return render(request, 'recetas/entradas.html')


#mostrar entradas

@login_required
def mostrarentradas(request):
    entradas = Entrada.objects.all()
    contexto = {"entradas":entradas}
    return render(request,"recetas/entradas.html",contexto)


#agregar entradas


def formularioEntrada(request):
    if request.method == 'POST':
        miFormulario = EntradaFormulario(request.POST)

        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
	
            entrada= Entrada(
            nombre_receta=informacion['nombre_receta'],
            duracion=informacion['duracion'],
            ingredientes=informacion['ingredientes'],
            procedimiento=informacion['procedimiento'],)

            entrada.save()
            
            entradas = Entrada.objects.all()
    
        return render(request,"recetas/entradas.html",{"entradas":entradas})
        
    else:
        miFormulario = EntradaFormulario()
        entradas=Entrada.objects.all()
    return render(request, "recetas/entradas.html", {"entradas": entradas, "miFormulario": miFormulario})


#editar entradas


def editarentrada(request,nombre_receta):

    entrada = Entrada.objects.get(nombre_receta = nombre_receta )

    if request.method == 'POST':
        miFormularioEntrada = EntradaFormulario(request.POST)
        print(miFormularioEntrada)

        if miFormularioEntrada.is_valid:
            
            informacion = miFormularioEntrada.cleaned_data
		
            entrada.nombre_receta=informacion['nombre_receta']
            entrada.duracion=informacion['duracion']
            entrada.ingredientes=informacion['ingredientes']
            entrada.procedimiento=informacion['procedimiento']
		
            entrada.save()
            
            return render(request, "recetas/index.html")

    else:
        miFormularioEntrada= EntradaFormulario(initial={'nombre_receta': entrada.nombre_receta, 'duracion': entrada.duracion , 
            'ingredeintes': entrada.ingredientes, 'procedimiento':entrada.procedimiento}) 
    
    return render(request, "recetas/editarentrada.html", {"miFormularioEntrada": miFormularioEntrada, "entrada_nombre":nombre_receta})


#eliminar entradas


def eliminarentrada(request,nombre_receta):
    entrada = Entrada.objects.get(nombre_receta=nombre_receta)
    entrada.delete()
    entradas = Entrada.objects.all()
    contexto ={"entradas":entradas}
    return render(request,"recetas/entradas.html",contexto)

@login_required
def buscarentrada(request):
    return render(request,"recetas/buscarentrada.html")
    

#buscar entradas


@login_required
def buscar(request):
        
    if request.GET["nombre_receta"]:
        nombre_receta = request.GET['nombre_receta']
        entradas = Entrada.objects.filter(nombre_receta__icontains=nombre_receta)
        
        return render(request, "receta/entradas.html",{"entradas":entradas})

    else:
        respuesta = "No se envío nada"
    return render(request,"recetas/index.html",{"respuesta":respuesta})


#-------------------------------Login/registro-----------------------------


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, "recetas/index.html", {"mensaje": f"Bienvenid@, {usuario}"})
        # Si los datos de autenticación son incorrectos, muestra el mensaje de error
        return render(request, "recetas/index.html", {"mensaje": "Datos incorrectos, inicie sesión nuevamente."})
    else:
        form = AuthenticationForm()
    return render(request, "recetas/login.html", {'form': form})
























def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"recetas/index.html",{"mensaje":"Usuario creado exitosamente"})
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
        miFormulario = UserEditForm(request.POST, instance=usuario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.username = informacion['username']  # Nuevo campo para modificar el nombre de usuario
            if informacion['password1']:
                usuario.set_password(informacion['password1'])
            usuario.save()
            return render(request, "recetas/index.html", {"mensaje": "Perfil actualizado correctamente"})
    else:
        miFormulario = UserEditForm(instance=usuario)
    return render(request, "recetas/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})




#@login_required
#def inicio(request):
    #avatares = Avatar.objects.filter(user=request.user.id)

    #return render(request,"recetas/base.html", {"url":avatares[0].imagen.url})


#--------------------------------------Plato principal--------------------------------------


#mostrar plato principal

@login_required
def mostrarplatoprincipal(request):
    platosprincipales = platoprincipal.objects.all()
    contexto = {"platosprincipales":platosprincipales}
    return render(request,"recetas/platos_principales.html",contexto)


#agregar entradas


def formularioPlato(request):
    if request.method == 'POST':
        miFormulario = PlatoprincipalFormulario(request.POST)

        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
	
            platoprincipal= Platoprincipal(
            nombre_receta=informacion['nombre_receta'],
            duracion=informacion['duracion'],
            ingredientes=informacion['ingredientes'],
            procedimiento=informacion['procedimiento'],)

            platoprincipal.save()
            
            platosprincipales = Platoprincipal.objects.all()
    
        return render(request,"recetas/plato_principal.html",{"platosprincipales":platosprincipales})
        
    else:
        miFormulario = PlatoprincipalFormulario()
        platosprincipales=Platoprincipal.objects.all()
    return render(request, "recetas/platos_principales.html", {"platosprincipales": platosprincipales, "miFormulario": miFormulario})


#editar entradas


def editarentrada(request,nombre_receta):

    entrada = Entrada.objects.get(nombre_receta = nombre_receta )

    if request.method == 'POST':
        miFormularioEntrada = EntradaFormulario(request.POST)
        print(miFormularioEntrada)

        if miFormularioEntrada.is_valid:
            
            informacion = miFormularioEntrada.cleaned_data
		
            entrada.nombre_receta=informacion['nombre_receta']
            entrada.duracion=informacion['duracion']
            entrada.ingredientes=informacion['ingredientes']
            entrada.procedimiento=informacion['procedimiento']
		
            entrada.save()
            
            return render(request, "recetas/entradas.html")

    else:
        miFormularioEntrada= EntradaFormulario(initial={'nombre_receta': entrada.nombre_receta, 'duracion': entrada.duracion , 
            'ingredientes': entrada.ingredientes, 'procedimiento':entrada.procedimiento}) 
    
    return render(request, "recetas/editarentrada.html", {"miFormularioEntrada": miFormularioEntrada, "entrada_nombre":nombre_receta})


#eliminar entradas


def eliminarentrada(request,nombre_receta):
    entrada = Entrada.objects.get(nombre_receta=nombre_receta)
    entrada.delete()
    entradas = Entrada.objects.all()
    contexto ={"entradas":entradas}
    return render(request,"recetas/entradas.html",contexto)

@login_required
def buscarentrada(request):
    return render(request,"recetas/buscarentrada.html")
    

#buscar entradas


@login_required
def buscar(request):
        
    if request.GET["nombre_receta"]:
        nombre_receta = request.GET['nombre_receta']
        entradas = Entrada.objects.filter(nombre_receta__icontains=nombre_receta)
        
        return render(request, "receta/entradas.html",{"entradas":entradas})

    else:
        respuesta = "No se envío nada"
    return render(request,"recetas/index.html",{"respuesta":respuesta})



def platoprincipal(request):
    return render(request,"recetas/platos_principales.html")

def postre(request):
    return render(request,"recetas/postres.html")

def singluten(request):
    return render(request,"recetas/singluten.html")

def vegano(request):
    return render(request,"recetas/veganos.html")
