
from recetas import views
from django.contrib.auth.views import LogoutView
from recetas.views import inicio, entrada, platoprincipal, postre, singluten, vegano, eliminarentrada, editarentrada, login, formularioEntrada, editarPerfil, formularioPlato, eliminarplato, editarplatoprincipal, formularioPostres, eliminarpostre, editarpostre, formularioVegano, eliminarvegano, editarvegano, formularioSingluten, eliminarsingluten, editarsingluten, buscarentrada
from django.urls import path


urlpatterns = [
    path('', inicio,name='index'),
    #--------------Entradas-----------------------
    path('entradas/', entrada ,name='entrada'),
    path('agregarentrada/',formularioEntrada, name='agregarentrada'),
    path('eliminarentradas/<nombre_receta>/', eliminarentrada,name='eliminarentrada'),
    path('editarentradas/<nombre_receta>/',editarentrada,name='editarentrada'),
    path('buscarentradas/',buscarentrada, name='buscarentrada'),
    #-----------Plato principal--------------------
    path('platos_principales/', platoprincipal ,name='platoprincipal'),
    path('agregarplatoprincipal/',formularioPlato, name='agregarplato'),
    path('eliminarplatoprincipal/<nombre_receta>/', eliminarplato,name='eliminarplato'),
    path('editarplato/<nombre_receta>/',editarplatoprincipal,name='editarplato'),
    #-----------Postre--------------------
    path('postres/', postre ,name='postre'),
    path('agregarpostre/',formularioPostres, name='agregarpostre'),
    path('eliminarpostre/<nombre_receta>/', eliminarpostre,name='eliminarpostre'),
    path('editarpostre/<nombre_receta>/',editarpostre,name='editarpostre'),
    #-----------Vegano--------------------
    path('veganos/', vegano ,name='vegano'),
    path('agregarvegano/',formularioVegano, name='agregarvegano'),
    path('eliminarvegano/<nombre_receta>/', eliminarvegano,name='eliminarvegano'),
    path('editarvegano/<nombre_receta>/',editarvegano,name='editarvegano'),
    #-----------Sin gluten--------------------
    path('singluten/', singluten ,name='singluten'),
    path('agregarsingluten/',formularioSingluten, name='agregarsingluten'),
    path('eliminarsingluten/<nombre_receta>/', eliminarsingluten,name='eliminarsingluten'),
    path('editarsingluten/<nombre_receta>/',editarsingluten,name='editarsingluten'),
    #--------------Login/Register--------------------
    path('login/',views.login_request, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',LogoutView.as_view(template_name='recetas/logout.html'), name='logout'),
    path('editarperfil/', editarPerfil, name="EditarPerfil"),

]