from django.db import models

# Create your models here.

class Dulce(models.Model):
    nombrereceta= models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} - {self.nombrereceta}"
    




