"""
------------------------------------------------------------------------------------------
class_views.py
Módulo Que contiene clases para el CRUD.
------------------------------------------------------------------------------------------
"""

# importo librerías a utilizar

from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .form import Repuestosform
from .models import Inventariosap
from .models import TemaConcreto,MailObservador
from django.http import HttpResponseRedirect



temarepuestos = Inventariosap()
#Agrego un primer mail de prueba como destinatario de correos
Observadores_a = MailObservador(temarepuestos)
Observadores_a.mail = 'alejolucerofenoglio@gmail.com'
#Agrego un segundo mail de prueba como destinatario de correos
Observadores_b = MailObservador(temarepuestos)
Observadores_b.mail = 'asfenoglio@fi.mdp.edu.ar'
temarepuestos.agregar(Observadores_a)
temarepuestos.agregar(Observadores_b)




class Repuesto_list(ListView):
    """
    Clase que realiza la visualización de repuestos
    en pantalla de inicio.
    """

    model = Inventariosap
    template_name = "inicio.html"

    def get_queryset(self):
        return self.model.objects.all().order_by("-id")[:10]


class Repuesto_crear(CreateView):
    """
    Clase que toma los datos ingresados por usuario, realiza el insert en
    la base de datos y retorna a la pantalla de inicio
    """
    model = Inventariosap
    form_class = Repuestosform
    template_name = "crear_repuesto.html"
    success_url = reverse_lazy("inicio")

'''
funcion para enviar mail

from django.conf import settings


def send_email(mail):
    Context = {'mail':mail}
    content = template.render(Context)
    email = EmailMultiAlternatives('Un correo de prueba','Alejo',
    setting.EMAIL_HOST_USER,
    [mail]
    )
    email.attach_alternative(content, 'text/html')
    email.send()

'''

class Repuesto_modificar(UpdateView):
    """
    Clase que nos permite modificar los datos de un repuesto,
    los actualiza en la base de datos y retorna a la pantalla de inicio
    """
    model = Inventariosap
    form_class = Repuestosform
    template_name = "crear_repuesto.html"
    success_url = reverse_lazy("inicio")


class Repuesto_eliminar(DeleteView):
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
        success_url = self.get_success_url()
        self.object.delete()
        temarepuestos.set_estado(1,self.object)
        return HttpResponseRedirect(success_url)
    
    
    

