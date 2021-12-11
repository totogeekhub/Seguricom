from django.contrib import admin
from .models import TipoEmpresa,Empresa,TipoRubro,Rubro,Contrato, Trabajador

# Register your models here.


admin.site.register(TipoEmpresa)
admin.site.register(Empresa)
admin.site.register(TipoRubro)
admin.site.register(Rubro)
admin.site.register(Contrato)
admin.site.register(Trabajador)