
from django.urls import path, include
from recetas import views
from django.contrib.auth.views import LogoutView
from recetas.views import inicio, entrada, platoprincipal, postre, singluten, vegano, mostrar_entradas, login

urlpatterns = [
    path('', inicio , name = "index"),
    path('entradas/', entrada, name= "entrada"),
    path('platosprincipales/', platoprincipal , name = "platoprincipal"),
    path('postres/', postre , name = "postre"),
    path('singluten/', singluten , name = "singluten"),
    path('veganos/', vegano , name = "vegano"),
    path('mostrarentradas/', mostrar_entradas, name = "entradas_list"),
    path('login/',views.login_request, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',LogoutView.as_view(template_name='recetas/logout.html'), name='logout'),
    path('editarPerfil/', views.editarPerfil, name="EditarPerfil")

]