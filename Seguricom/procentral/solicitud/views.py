import datetime
from django.contrib.auth import models
from django.db.models.fields import NullBooleanField
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Solicitud
from .forms import SoliForm
from django.db import connection
import cx_Oracle,datetime
from datetime import timedelta
from django.db.models.functions.datetime import Now

class StaffRequiredMixin(object):
    """
        Este Mixin requerira que el usuario sea miembro del staff
        """


    def dispatch(self, request, *args, **kwargs):
        if not request.user.level == 4 :
            print(request.user)
            return redirect(reverse_lazy('pages:pages'))
            
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


# Create your views here.


def update_solicit(request):



    if not request.user.level == 2 :

        return redirect(reverse_lazy('pages:pages'))
    data = {
        'solicitudes': listado_solicitudes_pendiente(),
        'tipos': listado_tipo_solicit(),
        'profes':listado_usuarios(),

    }
    date_str = datetime.datetime.today()

    #actualizar_solicitud(64,date_str,"respuesta automatizada",1,61)


    if request.method == "POST":
        id_solici = request.POST.get('solicitud')
        respuesta = request.POST.get('respuesta')
        profesional = request.POST.get('n_profe')
        check = request.POST.get('n_sino')


        if check == "0":
            actualizar_solicitud(id_solici,respuesta,0,profesional)
        if check == "1":
            actualizar_solicitud(id_solici,respuesta,1,profesional)
        if check == "2":
            actualizar_solicitud(id_solici,respuesta,2,profesional)

            

        """
        salida = actualizar_solicitud(id_solici,respuesta,estado_soli)
        if salida == 1:
            data['mensaje'] = 'Agregado correctamente' 
            
        else:
            data['mensaje'] = 'Nose pudo Agregar' 
        """


    return render(request,'solicitud/solicitud_update.html',data)


def solicitudesorcl(request):

    if not request.user.level == 2 and not request.user.level == 0 :
            return redirect(reverse_lazy('pages:pages'))
    data = {
        'solicitudes': listado_solicitudes(),
        'tipos': listado_tipo_solicit(),
    }
    

    return render(request,'solicitud/solicitud_list.html',data)


def solicitudespendientes(request):

    
    if not request.user.level == 2 and not request.user.level == 0 :
        return redirect(reverse_lazy('pages:pages'))
    

        
       

    data = {
        'solicitudes': listado_solicitudes_pendiente(),
        'tipos': listado_tipo_solicit(),
        'profes':listado_usuarios(),
    }

    
    if request.method == "POST":
        id_solici = request.POST.get('soli')
        respuesta = request.POST.get('respuesta')
        profesional = request.POST.get('n_profe')
        check = request.POST.get('n_sino')

        print(id_solici,respuesta,profesional,check)

        if check == "0":
            actualizar_solicitud(id_solici,respuesta,0,profesional)
            return redirect(reverse_lazy('solicits:solicits'))
        if check == "1":
            actualizar_solicitud(id_solici,respuesta,1,profesional)
            return redirect(reverse_lazy('solicits:aprobada'))
        if check == "2":
            actualizar_solicitud(id_solici,respuesta,2,profesional)
            return redirect(reverse_lazy('solicits:rechazada'))
        





    return render(request,'solicitud/solicitud_list.html',data)


def solicitudesapro(request):

    if not request.user.level == 2 and not request.user.level == 0 :
            return redirect(reverse_lazy('pages:pages'))

    data = {
        'solicitudes': listado_solicitudes_apro(),
        'tipos': listado_tipo_solicit(),
    }
    return render(request,'solicitud/solicitud_list.html',data)


def solicitudesrecha(request):

    if not request.user.level == 2 and not request.user.level == 0 :
            return redirect(reverse_lazy('pages:pages'))

    data = {
        'solicitudes': listado_solicitudes_recha(),
        'tipos': listado_tipo_solicit(),
    }
    return render(request,'solicitud/solicitud_list.html',data)


def solicitudescrear(request):

    if not request.user.level == 2 and not request.user.level == 0 :
            return redirect(reverse_lazy('pages:pages'))

    date_str = datetime.datetime.today()
    semana2 = date_str + timedelta(days=14)
    date = datetime.date.today().strftime('%Y-%m-%d')
    semana2_str = semana2.strftime('%Y-%m-%d')

    data = {
        'solicitudes': listado_solicitudes(),
        'tipos': listado_tipo_solicit(),
        'fecha_date': semana2_str ,
    }

    

    #agregar_solicitud(date_str,'YAPO CTM HACE LA SOLICITUD de visita',date_str,date_str,'0','2','0','2')

    if request.method == "POST":
        if semana2_str == request.POST.get('trip-start'):
            data['mensaje'] = 'fecha incorrecta' 


        descripcion = request.POST.get('descrip')
        usuario_id = request.user.id
        tipo_soli = request.POST.get('tipo_solicitud')
        fecha_act2 = request.POST.get('trip-start')
        hora_minuto = request.POST.get('horaminu')

        fecha_full = fecha_act2+hora_minuto
        
        salida = agregar_solicitud(fecha_full,descripcion,date_str,date_str,'0',usuario_id,'0',tipo_soli)
        
        if salida == 1:
            data['mensaje'] = 'Agregado correctamente' 
            
        else:
            data['mensaje'] = 'Nose pudo Agregar' 

    return render(request,'solicitud/solicitud_form.html',data)





def listado_solicitudes():




    django_cursor  =connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_solicitudes",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista





def listado_solicitudes_pendiente():
    django_cursor  =connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_solicitudes_filter_pendiente",[out_cur])

    lista = []
    for fila in out_cur:
        #print(lista)
        lista.append(fila)

    return lista




def listado_solicitudes_apro():
    django_cursor  =connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_solicitudes_filter_apro",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista





def listado_solicitudes_recha():
    django_cursor  =connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_solicitudes_filter_recha",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista



def listado_usuarios():
    django_cursor  =connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_profesionales",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista




def listado_tipo_solicit():
    django_cursor  =connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_solicitud_tipo",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista





def agregar_solicitud(a1,a2,a3,a4,a5,a6,a7,a8):
    django_cursor  =connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("sp_agregar_solicitud",[a1,a2,a3,a4,a5,a6,a7,a8,salida])
    return salida.getvalue()


def actualizar_solicitud(a1,a2,a3,a4):
    django_cursor  =connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("sp_actualizar_solicitud",[a1,a2,a3,a4,salida])
    return salida.getvalue()



class SoliListView(ListView):
    model = Solicitud
    

class SoliDetailView(DetailView):
    model = Solicitud

class SoliUpdate(UpdateView):
    model = Solicitud
    form_class = SoliForm
    template_name_suffix = '_update_form'
    template_name = 'solicitud/solicitud_update_form.html'

def get_success_url(self):
        return reverse_lazy('solicits:solicits')


class SoliCreateView(CreateView):
    model = Solicitud
    form_class = SoliForm
    success_url = reverse_lazy('solicits:solicits')

