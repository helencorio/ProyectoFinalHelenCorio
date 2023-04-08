
from recetas import views
from django.contrib.auth.views import LogoutView
from recetas.views import inicio, entrada, platoprincipal, postre, singluten, vegano, buscarentrada, eliminarentrada, mostrarentradas, editarentrada, login, formularioEntrada, editarPerfil
from django.urls import path


urlpatterns = [
    path('', inicio,name='index'),
    #--------------Entradas-----------------------
    path('entradas/', entrada ,name='entrada'),
    path('agregarentrada/',formularioEntrada,name='agregarentrada'),
    path('mostrarentradas/',mostrarentradas ,name='mostrarentradas'),
    path('eliminarentradas/<nombre_receta>/', eliminarentrada,name='eliminarentrada'),
    path('editarentradas/<nombre_receta>/',editarentrada,name='editarentrada'),
    path('buscarentrada/',buscarentrada,name='buscarentrada'),
    path('buscar/',views.buscar),
    #--------------Login/Register--------------------
    path('login/',views.login_request, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',LogoutView.as_view(template_name='recetas/logout.html'), name='logout'),
    path('editarperfil/', editarPerfil, name="EditarPerfil"),

    path('platoprincipal/', platoprincipal ,name='platoprincipal'),
    path('postres/', postre ,name='postre'),
    path('singluten/', singluten ,name='singluten'),
    path('vegano/', vegano ,name='vegano'),

]