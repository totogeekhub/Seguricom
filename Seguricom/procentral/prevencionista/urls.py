from django.urls import path
from .views import PrevenListView, PrevenDetailView,PrevenCreate,PrevenUpdate,PrevenDelete
from registration.views import SignUpView

preven_patterns = ([
    path('', PrevenListView.as_view(), name='prevencionistas'),   
    path('<int:pk>/<slug:slug>/', PrevenDetailView.as_view(), name='prevencionista'),
    #path('create/', PrevenCreate.as_view(), name='create'),
    path('update/<int:pk>/', PrevenUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PrevenDelete.as_view(), name='delete'),   
],'prevencionistas')