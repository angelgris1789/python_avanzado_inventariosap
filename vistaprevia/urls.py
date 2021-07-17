
'''
Definimos todas las urls contenidas en el proyecto

from django.urls import path
from django.contrib import admin
from vistaprevia.class_views import (
    Repuesto_eliminar,
    Repuesto_list,
    Repuesto_crear,
    Repuesto_modificar,
)



urlpatterns = [
    path("admin/", admin.site.urls), #panel de administrador
    path("", Repuesto_list.as_view(), name="inicio"), #path de inicio
    path("crear_repuesto", Repuesto_crear.as_view(), name="crear_repuesto"), #Creación de repuesto
    path("modificar_repuesto/<int:pk>/",Repuesto_modificar.as_view(),name="modificar_repuesto"), #Modificación de repuesto
    path("eliminar_repuesto/<int:pk>/", Repuesto_eliminar.as_view(),name="eliminar_repuesto"), #Eliminación de repuesto
]
'''

from django.urls import path
from django.contrib import admin
from vistaprevia.class_views import (
    Repuesto_eliminar,
    Repuesto_list,
    Repuesto_crear,
    Repuesto_modificar,
)


urlpatterns = [
    path("admin/", admin.site.urls), #panel de administrador
    path("", Repuesto_list.as_view(), name="inicio"), #path de inicio
    path("crear_repuesto", Repuesto_crear.as_view(), name="crear_repuesto"), #Creación de repuesto
    path("modificar_repuesto/<int:pk>/",Repuesto_modificar.as_view(),name="modificar_repuesto"), #Modificación de repuesto
    path("eliminar_repuesto/<int:pk>/", Repuesto_eliminar.as_view(),name="eliminar_repuesto"), #Eliminación de repuesto
]