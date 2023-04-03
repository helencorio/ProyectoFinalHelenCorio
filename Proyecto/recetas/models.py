from django.db import models

# Create your models here.

class Entrada(models.Model):
    nombre_receta= models.CharField(max_length=20)

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


