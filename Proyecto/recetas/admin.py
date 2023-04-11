from django.contrib import admin
from recetas.models import Entrada, Postre, Platoprincipal, Vegano, Singluten, Avatar

# Register your models here.
admin.site.register(Entrada)
admin.site.register(Postre)
admin.site.register(Platoprincipal)
admin.site.register(Vegano)
admin.site.register(Singluten)
admin.site.register(Avatar)
