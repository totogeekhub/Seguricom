from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import ActividadSoli
from django.contrib.admin.views.decorators import staff_member_required
from django.db import connection
import cx_Oracle,datetime
from django.db.models.functions.datetime import Now


# Create your views here.


def actividadList(request):
    usuario_id = request.user.id
    lista_s = listado_solicitudes()
    lista_a = listado_actividades()

    id_soli_list = []
    id_acti_list = []

    for x in lista_s:
        if x[6] == usuario_id:
            id_soli_list.append(x[0])
    print(id_soli_list)

    for y in lista_a:
        for z in id_soli_list:
            if y[7] == z:
                id_acti_list.append(y)
    print(id_acti_list)

    data = {
        'actividades':id_acti_list,
        'solicitudes':id_soli_list,
    } 


    return render(request,'actividad/actividad_list.html',data)




def listado_solicitud_idsoli(iduser):

    django_cursor  =connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("sp_listar_solicitudes_porid",[iduser,out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista




def listado_actividades():

    django_cursor  =connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("sp_listar_actividades",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def listado_solicitudes():

    django_cursor  =connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("sp_listar_solicitudes",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def listado_soli_iduser(iduser):

    django_cursor  =connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("sp_get_idsoli_poriduser",[iduser,out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


