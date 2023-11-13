"""
URL configuration for fruti_delicias project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#se importa tambien el include de django.urls import
from django.urls import include, path

#incluimos todas las urls que creamos en la app fruver
#las que estan en en el archivo fruver/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fruver.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
