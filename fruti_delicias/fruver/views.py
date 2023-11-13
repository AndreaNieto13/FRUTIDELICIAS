from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Categorias, Productos
from .forms import CategoriasForm, ProductosForm
from django.contrib.auth.decorators import login_required



#funcion que se le envia una solicitud y responde imprimiendo  el texto en H1
@login_required
def inicio (request):
    return render (request, 'paginas/inicio.html')

#funicion para localizar el archivo html en y cargarlo, el archivo se llama nosotros.html
#que se encuentra en templates/paginas
def nosotros (request):
    return render (request, 'paginas/nosotros.html')

def categorias (request):
    #cargamos del modelo todos los datos que tiene Categorias
    categorias = Categorias.objects.all()
    return render (request, 'modulos/categorias.html', {'categorias': categorias})



def productos (request):
    productos = Productos.objects.all()
    return render (request, 'modulos/productos.html',{'productos':productos})

def crear_categorias (request):
    formulario = CategoriasForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('categorias')
    
    return render (request, 'modulos/crear_categorias.html', {'formulario': formulario})

def crear_productos (request):
    formulario = ProductosForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render (request, 'modulos/crear_productos.html', {'formulario': formulario})


def login (request):
    return render (request, 'registration/login.html')