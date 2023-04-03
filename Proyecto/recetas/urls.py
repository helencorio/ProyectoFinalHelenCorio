
from django.urls import path, include
from recetas.views import inicio, entrada, platoprincipal, postre, singluten, vegano, mostrar_entradas, login

urlpatterns = [
    path('', inicio , name = "index"),
    path('entradas/', entrada, name= "entrada"),
    path('platosprincipales/', platoprincipal , name = "platoprincipal"),
    path('postres/', postre , name = "postre"),
    path('singluten/', singluten , name = "singluten"),
    path('veganos/', vegano , name = "vegano"),
    path('mostrarentradas/', mostrar_entradas, name = "entradas_list"),
    path('login/', login , name = "login"),

]