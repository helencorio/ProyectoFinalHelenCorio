from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from distutils.command.upload import upload

# Create your models here.

#---------------------------Entrada------------------
class Entrada(models.Model):
    nombre_receta= models.CharField(max_length=30)
    duracion= models.CharField(max_length=20, default= ' ')
    ingredientes= models.CharField(max_length=60, default= ' ')
    procedimiento= models.CharField(max_length=500, default= ' ')
    
    def __str__(self):
        return f"{self.nombre_receta} - {self.ingredientes} - {self.duracion}"
    

#---------------------------Entrada------------------

class Platoprincipal(models.Model):
    nombre_receta= models.CharField(max_length=20)
    duracion= models.CharField(max_length=20, default= ' ')
    ingredientes= models.CharField(max_length=60, default= ' ')
    procedimiento= models.CharField(max_length=500, default= ' ')

    def __str__(self):
        return f"{self.nombre_receta} - {self.ingredientes} - {self.duracion}"
    
class Postre(models.Model):
    nombre_receta= models.CharField(max_length=20)
    duracion= models.CharField(max_length=20, default= ' ')
    ingredientes= models.CharField(max_length=60, default= ' ')
    procedimiento= models.CharField(max_length=500, default= ' ')

    def __str__(self):
        return f"{self.nombre_receta} - {self.ingredientes} - {self.duracion}"

class Vegano(models.Model):
    nombre_receta= models.CharField(max_length=20)
    duracion= models.CharField(max_length=20, default= ' ')
    ingredientes= models.CharField(max_length=60, default= ' ')
    procedimiento= models.CharField(max_length=500, default= ' ')

    def __str__(self):
        return f"{self.nombre_receta} - {self.ingredientes} - {self.duracion}"
    
class Singluten(models.Model):
    nombre_receta= models.CharField(max_length=20)
    duracion= models.CharField(max_length=20, default= ' ')
    ingredientes= models.CharField(max_length=60, default= ' ')
    procedimiento= models.CharField(max_length=500, default= ' ')

    def __str__(self):
        return f"{self.nombre_receta} - {self.ingredientes} - {self.duracion}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares',null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
