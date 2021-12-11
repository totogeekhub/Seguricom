from django.urls import path
from django.views.generic.edit import DeleteView
from .views import pagar_web_pay

pagos_patterns = ([
    path('', pagar_web_pay, name='pago'),
],'pagos')