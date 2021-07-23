"""
------------------------------------------------------------------------------------------
class_views.py
Módulo Que contiene clases para el CRUD.
------------------------------------------------------------------------------------------
"""

# importo librerías a utilizar

from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from vistaprevia.form import Repuestosform
from vistaprevia.models import CellObservador, Inventariosap, Logobservador
from vistaprevia.models import MailObservador


temarepuestos = Inventariosap()
#Agrego un primer mail de prueba como destinatario de correos
Observadores_a = MailObservador(temarepuestos)
Observadores_a.mail = 'alejolucerofenoglio@gmail.com'
#Agrego un segundo mail de prueba como destinatario de correos
Observadores_b = MailObservador(temarepuestos)
Observadores_b.mail = 'asfenoglio@fi.mdp.edu.ar'
#Agrego un Observador como destinatario de mensjería por Whatsapp
Observadores_c = CellObservador(temarepuestos)
Observadores_c.numero = '54_92235655963'
#Agrego un Observador para registrar elimiaciones en un archivo txt
Observadores_d = Logobservador(temarepuestos)
Observadores_d.log = 'log_eliminaciones.txt'


class Repuestolist(ListView):
    """
    Clase que realiza la visualización de repuestos
    en pantalla de inicio.
    """

    model = Inventariosap
    template_name = "inicio.html"

    def get_queryset(self):
        return self.model.objects.all().order_by("-id")[:10]


class Repuestocrear(CreateView):
    """
    Clase que toma los datos ingresados por usuario, realiza el insert en
    la base de datos y retorna a la pantalla de inicio
    """
    model = Inventariosap
    form_class = Repuestosform
    template_name = "crear_repuesto.html"
    success_url = reverse_lazy("inicio")

class Repuestomodificar(UpdateView):
    """
    Clase que nos permite modificar los datos de un repuesto,
    los actualiza en la base de datos y retorna a la pantalla de inicio
    """
    model = Inventariosap
    form_class = Repuestosform
    template_name = "crear_repuesto.html"
    success_url = reverse_lazy("inicio")


class Repuestoeliminar(DeleteView):
    """
    Eliminar el repuesto y actualiza el listado en la pantalla de inicio
    """
    success_url = reverse_lazy("inicio")
    model = Inventariosap
    template_name = "verificacion.html"

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.

        Notifico eliminación a todos los observadores
        """
        self.object = self.get_object()
        self.object.delete()
        temarepuestos.set_estado('eliminación', self.object)
        return HttpResponseRedirect(self.success_url)
    