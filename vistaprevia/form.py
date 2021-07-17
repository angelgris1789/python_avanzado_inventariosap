'''
------------------------------------------------------------------------------------------
form.py
Módulo Que contiene clases para el CRUD.
------------------------------------------------------------------------------------------
'''

from django import forms
from .models import Inventariosap

class Repuestosform(forms.ModelForm):
    '''
    Defino nuestro form con todos los campos definidos
    en el modelo de Inventario
        class Meta:
        model = Inventariosap
        fields = '__all__'

    '''
    class Meta:
        model = Inventariosap
        fields = '__all__'
