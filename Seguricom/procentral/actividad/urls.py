from django.urls import path
from django.views.generic.edit import DeleteView
from .views import  actividadList




actividad_patterns = ([
    path('', actividadList, name='actividads'),

],'actividads')