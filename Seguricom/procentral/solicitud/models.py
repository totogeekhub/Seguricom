from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField 
from prevencionista.models import Prevencionista
from profesional.models import Profesional
from manager.models import Manager


# Create your models here.

class TipoSolicitud(models.Model):
    id_soli = models.AutoField(primary_key=True)
    nombre_soli = models.CharField(null=True, max_length=100, verbose_name="Tipo Solicitud")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    

    class Meta:
        verbose_name = "Tipo de solicitud"
        verbose_name_plural = "Tipo de solicitudes"
        ordering = ['order', 'nombre_soli']

    def __str__(self):
        return self.nombre_soli



class Solicitud(models.Model):
    id_soli = models.AutoField(primary_key=True,default=0)
    fecha_act = models.DateTimeField(null=True,blank=True,auto_now_add=True, verbose_name="Fecha de creación")
    descrip = models.TextField(blank=True,null=True,verbose_name="Descripcion",max_length=100)
    usuario_solicitante = models.ForeignKey(User , related_name="usua_soli",on_delete=models.PROTECT ,blank=True,verbose_name="Solicitante")
    respuesta = models.TextField( default="",blank=True,verbose_name="Respuesta",max_length=100)

    tipo_actividad = models.SmallIntegerField(verbose_name="Tipo Actividad", default=0)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    estado_soli = models.SmallIntegerField(verbose_name="Estado", default=0)

    tipo_solicitud = models.ForeignKey(TipoSolicitud,on_delete=models.PROTECT, default=0,blank=True,verbose_name="Tipo Solicitud")

    aprueba = models.OneToOneField(Manager,on_delete=models.PROTECT,blank=True,default=0)
    realiza = models.OneToOneField(Profesional,on_delete=models.PROTECT,blank=True,default=0)
    destinatario = models.OneToOneField(Prevencionista, on_delete=models.PROTECT,blank=True,default=0)

    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"
        ordering = ['estado_soli']

    def __str__(self):
        return self.descrip

    



