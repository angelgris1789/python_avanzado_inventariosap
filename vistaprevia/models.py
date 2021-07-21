from django.db import models
from django.core.mail import send_mail
import time
import pyautogui as pg
import webbrowser as web

"""
Se crea la clase inventario, con los datos relevantes
para nuestro CRUD
"""
class Tema():
    '''
    Defino tema para administrar los observadores y notificarlos ante
    el evento "trigger"
    '''
    def __init__(self):
        self._observers = []

    def agregar(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)

    def eliminar(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

        
    def notificar(self,obj):
        '''
        Recorro observadores para notificar sobre la baja del repuesto
        '''
        for observador in self._observers:
            observador.update(obj,observador.mail)

    def __str__(self):
        return self._observers


class TemaConcreto(Tema):
    '''
    Defino manejo de estado del objeto en cuestión para indicar la notificación 
    a los observadores
    '''
    def __init__(self):
        self.estado = None
        self._observers = []

    def set_estado(self, value, obj):
        self.estado = value
        self.notificar(obj)

    def get_estado(self):
        return self.estado 


class Observador():
    '''
    Defino lista de observers en blanco para su inicialización
    '''
    def __init__(self):
       self.observadores = []

    
class MailObservador(Observador):
    '''
    Defino la clase MailObservador para conformar el mensaje y enviar el mail
    ante la solicitud de actualización del objeto eliminado
    '''
    def __init__(self, obj):
        self.observadores = obj
        self.observadores.agregar(self)

    mail = ''

    def update(self, obj, mail):
        '''
        Actualizo novedad a observadores responsables del inventario vía mail
        '''
        mensaje = 'Se ha eliminado el repuesto '+str(obj)+' en forma definitiva.'
        send_mail('BAJA DE REPUESTO',mensaje,'alejolucerofenoglio@gmail.com',
            ['"'+mail+'"'],fail_silently=False)
        
    def __str__(self):
        return self.mail


class CellObservador(Observador):
    '''
    Defino la clase MailObservador para conformar el mensaje y enviar el mail
    ante la solicitud de actualización del objeto eliminado
    '''
    def __init__(self, obj):
        self.observadores = obj
        self.observadores.agregar(self)

    numero = ''
    mail = ''
    def update(self, obj, numero):
        '''
        Actualizo novedad a observadores responsables del inventario vía mail
        '''
        mensaje = 'Se ha eliminado el repuesto '+str(obj)+' en forma definitiva.'
        time.sleep(8)
        web.open('https://web.whatsapp.com/send?phone='+self.numero+'&text='+mensaje)
        pg.click(800,600)
        time.sleep(10)
        pg.press('enter')
        time.sleep(6)
        pg.hotkey('ctrl','w')
        time.sleep(10)
        
    def __str__(self):
        return self.mail


class Inventariosap(models.Model, TemaConcreto):
    
    
    codigosap = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=128)
    ubicacion = models.CharField(max_length=11, blank=True, null=False)
    cantidad = models.IntegerField()
    costounitario = models.IntegerField()
    
    def __str__(self):
        '''
        Conformo detalles del repuesto a enviar vía mail y a mostrar en mensaje de confirmación
        para eliminarlo definitivamente de la base de datos
        '''
        mensaje = str(self.codigosap)+': '+str(self.descripcion)+' || Cantidad: '+str(self.cantidad)
        return mensaje

