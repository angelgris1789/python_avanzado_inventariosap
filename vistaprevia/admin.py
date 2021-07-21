'''
admin.py
Módulo de vista de administrador, con
sus respectivos filtros de búsqueda
'''

from django.contrib import admin
from vistaprevia.models import Inventariosap

class Inventarioadmin(admin.ModelAdmin):
    '''
    Clase que define diplays y filtros en la vista de administrador
    '''
    list_display = [
        "codigosap",
        "descripcion",
        "ubicacion",
        "costounitario",
        "cantidad"
        ]
    list_filter = [
        "codigosap",
        "descripcion",
        "ubicacion"
        ]

admin.site.register(Inventariosap, Inventarioadmin)
