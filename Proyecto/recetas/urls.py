
from django.urls import path, include
from recetas.views import inicio

urlpatterns = [
    path('', inicio , name = "index")
]