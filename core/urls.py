from django.urls import path

from .views import *
urlpatterns=[
   path('login/', LoginView.as_view(), name='login'),
   path('dashboard/', dashboard, name='dashboard'),
   path('colaboradorNew/',ColaboradorCreate.as_view(), name='colaboradorNew'),
   path('colaboradorLista/',ColabList.as_view(), name='colabList'),
]