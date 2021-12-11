from django.db import models
from django.db.models.base import Model
from ckeditor.fields import RichTextField
from django.db.models.fields import CharField
from django.db.models.fields.related import OneToOneField
from manager.models import Manager
from django.db.models.deletion import PROTECT

# Create your models here.


class TipoEmpresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre_emp = models.CharField(null=True, max_length=100, verbose_name="Tipo Empresa")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Tipo de Empresa"
        verbose_name_plural = "Tipo de Empresas"
        ordering = ['order', 'nombre_emp']

    def __str__(self):
        return self.nombre_emp


class TipoRubro(models.Model):
    
    name_rubro = models.CharField(null=True, max_length=100, verbose_name="Nombre Rubro")
    descripcion = models.TextField(verbose_name="Descripcion", max_length=150)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Tipo de Rubro"
        verbose_name_plural = "Tipo de Rubros"
        ordering = ['order', 'name_rubro']

    def __str__(self):
        return self.name_rubro

class Empresa(models.Model):
    rut_emp = models.CharField(max_length=15, verbose_name="Rut (sin puntos con guion)")
    nombre_emp = models.CharField(null=True, max_length=100, verbose_name="Nombre Empresa")
    direccion_emp = models.TextField( max_length=100, verbose_name="Direccion Empresa")
    fono_emp = models.CharField(max_length=15,verbose_name="Telefono")
    email_emp = models.EmailField(blank=True,verbose_name="Correo electronico")
    estado_emp = models.BooleanField(verbose_name="Estado Empresa")
    razon_social_emp = models.CharField( max_length=100, verbose_name="Razon social")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)



    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ['order', 'nombre_emp']

    def __str__(self):
        return self.nombre_emp

class Rubro(models.Model):
    nombre = models.CharField(null=True, max_length=100, verbose_name="Nombre del Rubro")
    descripcion = RichTextField(verbose_name="Contenido")
    tipo_rubro = models.OneToOneField(TipoRubro, on_delete=models.PROTECT)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)


    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Rubro"
        verbose_name_plural = "Rubros"
        ordering = ['order', 'nombre']

    def __str__(self):
        return self.nombre




class Contrato(models.Model):
    empresa = models.OneToOneField(Empresa, on_delete=models.PROTECT)
    manager = models.OneToOneField(Manager, on_delete=models.PROTECT)
    rubro = models.OneToOneField(Rubro, on_delete=models.PROTECT)
    name = models.CharField(max_length=100,verbose_name="Nombre")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    estado = models.BooleanField(verbose_name="Estado Empresa")
    descripcion = RichTextField(verbose_name="Contenido")
    fecha_inicio = models.DateField(blank=True, verbose_name="Fecha de Inicio")
    fecha_termino = models.DateField(blank=True, verbose_name="Fecha de Termino")


    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name




class Trabajador(models.Model):
    nombres = models.CharField(max_length=200,verbose_name="Nombres")
    apellido_pat = models.CharField(max_length=200,verbose_name="Apellido Paterno")
    apellido_mat = models.CharField(max_length=200,verbose_name="Apellido Materno")
    run = models.CharField(max_length=15, verbose_name="Run Trabajador")
    orden = models.SmallIntegerField(verbose_name="Orden", default=0)
    empresa = models.OneToOneField(Empresa,blank=True,on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"
        ordering = ['orden', 'nombres']

    def __str__(self):
        return self.nombres
