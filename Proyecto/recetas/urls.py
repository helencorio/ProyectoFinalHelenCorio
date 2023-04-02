
from django.urls import path, include
from recetas.views import inicio, base

urlpatterns = [
    path('', inicio , name = "index"),
    path('entradas/', base, name= "entradas")
]