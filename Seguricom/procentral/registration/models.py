from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import TextChoices
from django.db.models.fields import TextField
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save

from empresa.models import TipoEmpresa

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True, verbose_name="Foto")
    bio = TextField(null=True,blank=True,verbose_name="Biografia")
    link = models.URLField(max_length=200, null=True, blank=True,verbose_name="Red Social")
    rubro = models.ForeignKey(TipoEmpresa,on_delete=CASCADE,null=True,blank=True,verbose_name="Empresa") 
    telefono = models.TextField(null=True,blank=True,verbose_name="Contacto")
    nivel_profile = models.SmallIntegerField(verbose_name="Nivel ", default=0)
    
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        ordering = ['user__username']

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su perfil enlazado")


