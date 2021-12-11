from django.contrib import admin
from .models import ActividadSoli, Tipoactividad,Visita,Capacitacion,Asesoria,FiscalizacionAsesoria,AccidenteAsesoria
# Register your models here.

admin.site.register(Tipoactividad)
admin.site.register(ActividadSoli)
admin.site.register(Visita)
admin.site.register(Capacitacion)
admin.site.register(Asesoria)
admin.site.register(FiscalizacionAsesoria)
admin.site.register(AccidenteAsesoria)