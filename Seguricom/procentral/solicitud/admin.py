from django.contrib import admin
from .models import Solicitud,TipoSolicitud

# Register your models here.
admin.site.register(Solicitud)
admin.site.register(TipoSolicitud)