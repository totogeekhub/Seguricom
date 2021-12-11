from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.db import connection
import cx_Oracle,datetime
from django.db.models.functions.datetime import Now


# Create your views here.


def pagar_web_pay(request):

    return render(request,'webpay_pago/pagar_form.html')
    