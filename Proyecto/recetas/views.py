from django.shortcuts import render
from django.http import HttpResponse
from recetas.forms import EntradaFormulario,UserRegisterForm,UserEditForm, PlatoprincipalFormulario, PostreFormulario, SinglutenFormulario, VeganoFormulario
from recetas.models import Entrada, Platoprincipal, Avatar, Postre, Singluten, Vegano
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
@login_required
def entrada(request):
    entradas = Entrada.objects.all()
    return render(request, 'recetas/entradas.html', {'entradas': entradas})



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
    
    return render(request, "recetas/agregarentrada.html", {"entradas": entradas, "miFormulario": miFormulario})


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
            entradas = Entrada.objects.all()
            
            return render(request,"recetas/entradas.html",{"entradas":entradas})

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

    

#buscar entradas


def buscarentrada(request):
    entradas = []
    nombre_receta = ""
    if "nombre_receta" in request.GET:
        nombre_receta = request.GET['nombre_receta']
        entradas = Entrada.objects.filter(nombre_receta__icontains=nombre_receta)
    return render(request, "recetas/buscarentradas.html", {"entradas": entradas, "nombre_receta": nombre_receta})



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
    return render(request, "recetas/editarperfil.html", {"miFormulario": miFormulario, "usuario": usuario})


#--------------------------------------Avatar--------------------------------------


def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    if avatares:
        url = avatares[0].imagen.url
    else:
        url = ""

    return render(request, "recetas/index.html", {"url": url})


#--------------------------------------Plato principal--------------------------------------


#mostrar plato principal

@login_required
def mostrarplatoprincipal(request):
    platosprincipales = platoprincipal.objects.all()
    contexto = {"platosprincipales":platosprincipales}
    return render(request,"recetas/platos_principales.html",contexto)


#agregar plato principal


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
    
        return render(request,"recetas/platos_principales.html",{"platosprincipales":platosprincipales})
        
    else:
        miFormulario = PlatoprincipalFormulario()
        platosprincipales=Platoprincipal.objects.all()
    return render(request, "recetas/agregarplatoprincipal.html", {"platosprincipales": platosprincipales, "miFormulario": miFormulario})


#editar entradas


def editarplatoprincipal(request,nombre_receta):

    platoprincipal = Platoprincipal.objects.get(nombre_receta = nombre_receta )

    if request.method == 'POST':
        miFormularioPlato = PlatoprincipalFormulario(request.POST)
        print(miFormularioPlato)

        if miFormularioPlato.is_valid():
            
            informacion = miFormularioPlato.cleaned_data
		
            platoprincipal.nombre_receta=informacion['nombre_receta']
            platoprincipal.duracion=informacion['duracion']
            platoprincipal.ingredientes=informacion['ingredientes']
            platoprincipal.procedimiento=informacion['procedimiento']
		
            platoprincipal.save()
            
            return render(request, "recetas/platos_principales.html", {"platosprincipales": Platoprincipal.objects.all()})

    else:
        miFormularioPlato= PlatoprincipalFormulario(initial={'nombre_receta': platoprincipal.nombre_receta, 'duracion': platoprincipal.duracion , 
            'ingredientes': platoprincipal.ingredientes, 'procedimiento':platoprincipal.procedimiento}) 
    
    return render(request, "recetas/editarplatoprincipal.html", {"miFormularioPlato": miFormularioPlato, "plato_nombre":nombre_receta})


#eliminar plato principal


def eliminarplato(request,nombre_receta):
    platosprincipales = Platoprincipal.objects.get(nombre_receta=nombre_receta)
    platosprincipales.delete()
    platosprincipales = Platoprincipal.objects.all()
    contexto ={"platosprincipales":platosprincipales}
    return render(request,"recetas/platos_principales.html",contexto)

    

@login_required
def platoprincipal(request):
    platosprincipales = Platoprincipal.objects.all()
    return render(request, 'recetas/platos_principales.html', {'platosprincipales': platosprincipales})


#--------------------------------------Postre--------------------------------------

def postre(request):
    postres = Postre.objects.all()
    return render(request, 'recetas/postres.html', {'postres': postres})



#mostrar postres

@login_required
def mostrarpostres(request):
    postres = Postre.objects.all()
    contexto = {"postres":postres}
    return render(request,"recetas/postres.html",contexto)


#agregar postres


def formularioPostres(request):
    if request.method == 'POST':
        miFormulario = PostreFormulario(request.POST)

        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
	
            postre= Postre(
            nombre_receta=informacion['nombre_receta'],
            duracion=informacion['duracion'],
            ingredientes=informacion['ingredientes'],
            procedimiento=informacion['procedimiento'],)

            postre.save()
            
            postres = Postre.objects.all()
    
        return render(request,"recetas/postres.html",{"postres":postres})
        
    else:
        miFormulario = PostreFormulario()
        postres=Postre.objects.all()
    return render(request, "recetas/agregarpostre.html", {"postres": postres, "miFormulario": miFormulario})


#editar entradas


def editarpostre(request,nombre_receta):

    postre = Postre.objects.get(nombre_receta = nombre_receta )

    if request.method == 'POST':
        miFormularioPostre = PostreFormulario(request.POST)
        print(miFormularioPostre)

        if miFormularioPostre.is_valid:
            
            informacion = miFormularioPostre.cleaned_data
		
            postre.nombre_receta=informacion['nombre_receta']
            postre.duracion=informacion['duracion']
            postre.ingredientes=informacion['ingredientes']
            postre.procedimiento=informacion['procedimiento']
		
            postre.save()
            postres = Postre.objects.all()
            
            return render(request, "recetas/postres.html", {"postres": postres})

    else:
        miFormularioPostre= PostreFormulario(initial={'nombre_receta': postre.nombre_receta, 'duracion': postre.duracion , 
            'ingredientes': postre.ingredientes, 'procedimiento':postre.procedimiento}) 
    
    return render(request, "recetas/editarpostre.html", {"miFormularioPostre": miFormularioPostre, "postre_nombre":nombre_receta})


#eliminar plato principal


def eliminarpostre(request,nombre_receta):
    postres = Postre.objects.get(nombre_receta=nombre_receta)
    postres.delete()
    postres = Postre.objects.all()
    contexto ={"postres":postres}
    return render(request,"recetas/postres.html",contexto)

#--------------------------------------Sin gluten--------------------------------------

def singluten(request):
    singluten = Singluten.objects.all()
    return render(request, 'recetas/singluten.html', {'singluten': singluten})

@login_required
def mostrarsingluten(request):
    singluten = Singluten.objects.all()
    contexto = {"singluten":singluten}
    return render(request,"recetas/singluten.html",contexto)



def formularioSingluten(request):
    if request.method == 'POST':
        miFormulario = SinglutenFormulario(request.POST)

        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
	
            singlu= Singluten(
            nombre_receta=informacion['nombre_receta'],
            duracion=informacion['duracion'],
            ingredientes=informacion['ingredientes'],
            procedimiento=informacion['procedimiento'],)

            singlu.save()
            
            singluten = Singluten.objects.all()
    
        return render(request,"recetas/singluten.html",{"singluten":singluten})
        
    else:
        miFormulario = SinglutenFormulario()
        singluten=Singluten.objects.all()
    return render(request, "recetas/agregarsingluten.html", {"singluten": singluten, "miFormulario": miFormulario})




def editarsingluten(request,nombre_receta):

    singlu = Singluten.objects.get(nombre_receta = nombre_receta )

    if request.method == 'POST':
        miFormularioSingluten = SinglutenFormulario(request.POST)
        print(miFormularioSingluten)

        if miFormularioSingluten.is_valid():
            
            informacion = miFormularioSingluten.cleaned_data
		
            singlu.nombre_receta=informacion['nombre_receta']
            singlu.duracion=informacion['duracion']
            singlu.ingredientes=informacion['ingredientes']
            singlu.procedimiento=informacion['procedimiento']
		
            singlu.save()
            singluten = Singluten.objects.all()
            
            return render(request, "recetas/singluten.html", {"singluten": singluten})

    else:
        miFormularioSingluten= SinglutenFormulario(initial={'nombre_receta': singlu.nombre_receta, 'duracion': singlu.duracion , 
            'ingredientes': singlu.ingredientes, 'procedimiento':singlu.procedimiento}) 
    
    return render(request, "recetas/editarsingluten.html", {"miFormularioSingluten": miFormularioSingluten, "singluten_nombre":nombre_receta})




def eliminarsingluten(request,nombre_receta):
    singluten = Singluten.objects.get(nombre_receta=nombre_receta)
    singluten.delete()
    singluten = Singluten.objects.all()
    contexto ={"singluten":singluten}
    return render(request,"recetas/singluten.html",contexto)


#--------------------------------------Vegano--------------------------------------

def vegano(request):
    veganos = Vegano.objects.all()
    return render(request, 'recetas/veganos.html', {'veganos': veganos})

@login_required
def mostrarvegano(request):
    veganos = Vegano.objects.all()
    contexto = {"veganos":veganos}
    return render(request,"recetas/veganos.html",contexto)

def formularioVegano(request):
    if request.method == 'POST':
        miFormulario = VeganoFormulario(request.POST)

        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
	
            vegano= Vegano(
            nombre_receta=informacion['nombre_receta'],
            duracion=informacion['duracion'],
            ingredientes=informacion['ingredientes'],
            procedimiento=informacion['procedimiento'],)

            vegano.save()
            
            veganos = Vegano.objects.all()
    
        return render(request,"recetas/veganos.html",{"veganos":veganos})
        
    else:
        miFormulario = VeganoFormulario()
        veganos=Vegano.objects.all()
    return render(request, "recetas/agregarvegano.html", {"veganos": veganos, "miFormulario": miFormulario})


def editarvegano(request,nombre_receta):

    vegano = Vegano.objects.get(nombre_receta = nombre_receta )

    if request.method == 'POST':
        miFormularioVegano = VeganoFormulario(request.POST)
        print(miFormularioVegano)

        if miFormularioVegano.is_valid():
            
            informacion = miFormularioVegano.cleaned_data
		
            vegano.nombre_receta=informacion['nombre_receta']
            vegano.duracion=informacion['duracion']
            vegano.ingredientes=informacion['ingredientes']
            vegano.procedimiento=informacion['procedimiento']
		
            vegano.save()
            veganos = Vegano.objects.all()
            
            return render(request, "recetas/veganos.html", {"veganos": veganos})

    else:
        miFormularioVegano= VeganoFormulario(initial={'nombre_receta': vegano.nombre_receta, 'duracion': vegano.duracion , 
            'ingredientes': vegano.ingredientes, 'procedimiento':vegano.procedimiento}) 

    return render(request, "recetas/editarvegano.html", {"miFormularioVegano": miFormularioVegano, "vegano_nombre":nombre_receta})


def eliminarvegano(request,nombre_receta):
    veganos = Vegano.objects.get(nombre_receta=nombre_receta)
    veganos.delete()
    veganos = Vegano.objects.all()
    contexto ={"veganos":veganos}
    return render(request,"recetas/veganos.html",contexto)