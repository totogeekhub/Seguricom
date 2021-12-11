from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.

class HomePageView(TemplateView):
    template_name  = "core/home.html" 
    
    def get(self, request, *args,**kwargs):
        return render(request, self.template_name,{'title':"Mi Super web Playground"})


class SamplePageView(TemplateView):
    template_name  = "core/sample.html"