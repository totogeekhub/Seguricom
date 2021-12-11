from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import TextChoices
from django.db.models.fields import TextField
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save
from empresa.models import Empresa
from ckeditor.fields import RichTextField

class Prevencionista(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    empresa = models.OneToOneField(Empresa, on_delete=models.PROTECT)
    run = models.CharField(max_length=15, verbose_name="Run Prevencionista")


    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")



    
    
    class Meta:
        verbose_name = "Prevencionista"
        verbose_name_plural = "Prevencionistas"
        ordering = ['user__username']

    def __str__(self):
        return self.user.username

"""
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Prevencionista.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su perfil enlazado")
"""