from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import TextChoices
from django.db.models.fields import TextField
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profesional (models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    run = models.CharField(max_length=15, verbose_name="Run Prevencionista")
    cargo = models.CharField(verbose_name=("Descripcion del Cargo"), max_length=100)
    fecha_ingreso = models.DateField(blank=True, verbose_name="Fecha de Ingreso")
    fecha_termino = models.DateField(blank=True, verbose_name="Fecha de Termino")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"
        ordering = ['user__username']

    def __str__(self):
        return self.user.username