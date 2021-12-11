from django.urls import path
from .views import ProfeListView, ProfeDetailView,ProfeUpdate,ProfeDelete
from registration.views import SignUpView

profe_patterns = ([
    path('', ProfeListView.as_view(), name='profesionales'),   
    path('<int:pk>/<slug:slug>/', ProfeDetailView.as_view(), name='profesional'),
    #path('create/', ProfeCreate.as_view(), name='create'),
    path('update/<int:pk>/', ProfeUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ProfeDelete.as_view(), name='delete'),   
],'profesionales')