from django.urls import path
from .views import DefaListView, DefaDetailView,DefaUpdate,DefaDelete,DefaCreate


defa_patterns = ([
    path('', DefaListView.as_view(), name='udefaults'),   
    path('<int:pk>/<slug:slug>/', DefaDetailView.as_view(), name='udefault'),
    path('create/', DefaCreate.as_view(), name='create'),
    path('update/<int:pk>/', DefaUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', DefaDelete.as_view(), name='delete'),   
],'udefaults')