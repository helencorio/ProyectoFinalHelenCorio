from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entrada(models.Model):
    nombre_receta= models.CharField(max_length=30)
    duracion= models.IntegerField(default=0)
    ingredientes= models.CharField(max_length=60, default= ' ')
    procedimiento= models.CharField(max_length=500, default= ' ')


    def __str__(self):
        return f"{self.id} - {self.nombre_receta}"
    

class Platoprincipal(models.Model):
    nombre_receta= models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} - {self.nombre_receta}"
    
class Postre(models.Model):
    nombre_receta= models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} - {self.nombre_receta}"

class Vegano(models.Model):
    nombre_receta= models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} - {self.nombre_receta}"
    
class Singluten(models.Model):
    nombre_receta= models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} - {self.nombre_receta}"

#class Avatar(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #imagen = models.ImageField(upload_to='avatares',null=True, blank = True)
