from django.urls import path
from django.views.generic.edit import DeleteView
from .views import  SoliDetailView, SoliListView,SoliCreateView,solicitudesorcl,solicitudescrear,SoliUpdate,update_solicit,solicitudespendientes,solicitudesapro,solicitudesrecha




solicits_patterns = ([
    path('', solicitudesorcl, name='solicits'),
    path('pend/', solicitudespendientes, name='pendiente'),
    path('apro/', solicitudesapro, name='aprobada'),
    path('recha/', solicitudesrecha, name='rechazada'),
    path('solicit/', update_solicit, name="solicit"),
    path('create/', solicitudescrear, name='create'),
    path('update/<int:pk>/', SoliUpdate.as_view(), name='update'),
],'solicits')

