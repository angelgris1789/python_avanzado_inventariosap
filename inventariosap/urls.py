#urls.py
"""librosonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from vistaprevia.class_views import Repuesto_crear, Repuesto_eliminar, Repuesto_list, Repuesto_modificar


'''
Rutas de urls de: pantalla de inicio, crear, modificar y eliminar
repuestos del Inventario
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Repuesto_list.as_view(),name='inicio'),
    path('crear_repuesto',Repuesto_crear.as_view(), name='crear_repuesto'),
    path('modificar_repuesto/<int:pk>/',Repuesto_modificar.as_view(),name='modificar_repuesto'),
    path('eliminar_repuesto/<int:pk>/',Repuesto_eliminar.as_view(),name='eliminar_repuesto')

]
