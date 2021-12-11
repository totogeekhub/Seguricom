from django.db import models
from ckeditor.fields import RichTextField
from django.utils import tree
from actividad.models import Tipoactividad
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.deletion import CASCADE
from django.db.models.deletion import PROTECT


class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    tipo_act = models.ForeignKey(Tipoactividad,on_delete=models.PROTECT,null=True,blank=True,verbose_name="Actividad") 

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

