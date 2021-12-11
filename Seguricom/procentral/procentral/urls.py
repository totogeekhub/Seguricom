"""procentral URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from pages.urls import pages_patterns
from solicitud.urls import solicits_patterns
from actividad.urls import actividad_patterns
from webpay_pago.urls import pagos_patterns
from messenger.urls import messenger_patterns
from profiles.urls import profiles_patterns
from prevencionista.urls import preven_patterns
from profesional.urls import profe_patterns
from userdefault.urls import defa_patterns


from procentral.settings import MEDIA_URL

urlpatterns = [

    path('',include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),

    path('pages/', include(pages_patterns)),
    path('solicits/',include(solicits_patterns)),
    path('actividads/',include(actividad_patterns)),
    path('pagos/',include(pagos_patterns)),
    path('messenger/', include(messenger_patterns)),
    path('profiles/', include(profiles_patterns)),
    path('prevencionistas/', include(preven_patterns)),
    path('profesionales/', include(profe_patterns)),
    path('udefaults/', include(defa_patterns)),


   # path('activitys/', include('actividad.urls')),


    
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)