from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import BooleanField, CharField, EmailField
from solicitud.models import Solicitud
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField
from django.db.models.fields.related import OneToOneField
from django.db.models.deletion import PROTECT


# Create your models here.


class Tipoactividad(models.Model):
    id_act = models.AutoField(primary_key=True)
    nombre_act = models.CharField(null=True, max_length=100, verbose_name="Tipo Empresa")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    

    class Meta:
        verbose_name = "Tipo de actividad"
        verbose_name_plural = "Tipo de actividades"
        ordering = ['order', 'nombre_act']

    def __str__(self):
        return self.nombre_act


class ActividadSoli(models.Model):
    name = models.CharField(null=True,blank=True, max_length=100, verbose_name="Nombre de la Actividad")
    id_act_soli = models.AutoField(primary_key=True)
    tipo_act = models.ForeignKey(Tipoactividad,on_delete=models.PROTECT, default=0 ,null=True,blank=True,verbose_name="Actividad")    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    full_fecha_actividad = models.DateTimeField(auto_now=True,verbose_name="Fecha y Hora de la Actividad")
    estado_act = models.SmallIntegerField(verbose_name="Estado", default=0)
    

    sub_estado = models.BooleanField(verbose_name="Sub Estado",default=False)


    

    profesional = models.ForeignKey(User,default=0,on_delete=models.PROTECT)
    solicitud = models.OneToOneField(Solicitud,null=True, on_delete=models.PROTECT)


    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ['created', 'estado_act']

    def __str__(self):
        return self.name





class Visita(models.Model):

    actividad = models.OneToOneField(ActividadSoli, on_delete=models.PROTECT)
    descrip_inicio = models.TextField(max_length=150,verbose_name="Contenido")
    estado = models.SmallIntegerField(verbose_name="Orden", default=0)
    name = models.CharField(null=True, max_length=100, verbose_name="Nombre de la Visita")
    descrip_cierre = models.TextField(max_length=150,verbose_name="Informacion Ciere",blank=True)

    sub_estado = models.BooleanField(verbose_name="Sub Estado",default=False)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


    class Meta:
        verbose_name = "Visita"
        verbose_name_plural = "Visitas"
        ordering = ['created', 'name']

    def __str__(self):
        return self.name

class Capacitacion(models.Model):

    actividad = models.OneToOneField(ActividadSoli, on_delete=models.PROTECT)
    descripcion_inicio = models.TextField(max_length=150,verbose_name="Contenido")
    estado = models.SmallIntegerField(verbose_name="Orden", default=0)
    name = models.CharField(null=True, max_length=100, verbose_name="Nombre de la Capacitacion")
    materiales = models.TextField(null=True, max_length=100, verbose_name="Materiales")
    costo = models.CharField(max_length=7,verbose_name="Costo de Materiales")
    nro_asistentes = models.IntegerField(verbose_name="Numero de Asistentes")
    descrip_cierre = models.TextField(max_length=150,verbose_name="Informacion Ciere",blank=True)

    sub_estado = models.BooleanField(verbose_name="Sub Estado",default=False)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


    class Meta:
        verbose_name = "Capacitacion"
        verbose_name_plural = "Capacitaciones"
        ordering = ['created', 'name']

    def __str__(self):
        return self.name


class Asesoria(models.Model):
    name = models.CharField(null=True, max_length=100, verbose_name="Nombre de la Asesoria")
    actividad = models.OneToOneField(ActividadSoli, on_delete=models.PROTECT)
    descripcion_inicio = models.TextField(max_length=150,verbose_name="Contenido")
    estado = models.SmallIntegerField(verbose_name="Estado", default=0)
    descrip_cierre = models.TextField(max_length=150,verbose_name="Informacion Ciere",blank=True)

    sub_estado = models.BooleanField(verbose_name="Sub Estado",default=False)



    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


    class Meta:
        verbose_name = "Asesoria"
        verbose_name_plural = "Asesorias"
        ordering = ['actividad', 'created']

    def __str__(self):
        return self.name


class FiscalizacionAsesoria(models.Model):
    aseso = models.OneToOneField(Asesoria,on_delete=models.PROTECT)
    name_fiscalizador = models.CharField(max_length=100 ,verbose_name="Nombre del Fiscalizador")
    email_fiscalizador = models.EmailField(blank=True)
    estado = models.SmallIntegerField(verbose_name="Estado", default=0)
    descrip = models.TextField(max_length=150,verbose_name="Contenido")

    sub_estado = models.BooleanField(verbose_name="Sub Estado",default=False)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Fiscalizacion"
        verbose_name_plural = "Fiscalizaciones"
        ordering = ['aseso', 'created']

    def __str__(self):
        return self.aseso.name


class AccidenteAsesoria(models.Model):
    aseso = models.OneToOneField(Asesoria,on_delete=models.PROTECT)
    causa = models.TextField(max_length=150,verbose_name="Causa")
    estado = models.SmallIntegerField(verbose_name="Estado", default=0)
    descrip = models.TextField(max_length=150,verbose_name="Contenido")

    sub_estado = models.BooleanField(verbose_name="Sub Estado",default=False)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Accidente"
        verbose_name_plural = "Accidentes"
        ordering = ['aseso', 'created']

    def __str__(self):
        return self.aseso.name




