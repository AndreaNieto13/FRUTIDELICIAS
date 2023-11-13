from django.contrib import admin
from .models import Categorias, Productos #Importamos las clases que estan en el modelo

admin.site.register(Categorias)
admin.site.register(Productos)

