from django.urls import include, path
from . import views
#views de autenticacion para el login
from django.contrib.auth import views as auth_views
# el usuaro puede acceder a la vista de las urls
urlpatterns = [
  path('', views.login, name='login'),
    path('inicio', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('categorias', views.categorias, name='categorias'),
    path('productos', views.productos, name='productos'),
    path('categorias/crear', views.crear_categorias, name='crear_categorias'),
    path('productos/crear', views.crear_productos, name='crear_productos'),


]
