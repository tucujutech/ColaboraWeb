from django.urls import path

from .views import *
urlpatterns=[
   path('login/', LoginView.as_view(), name='login'),
   path('dashboard/', dashboard, name='dashboard'),
   path('colaboradorNew/',ColaboradorCreate.as_view(), name='colaboradorNew'),
   path('colaboradorLista/',ColabList.as_view(), name='colabList'),
   path('formacaoRegister/', FormacaoView.as_view(), name='formacaoRegister'),
   path('formacaoList/', FormacaoList.as_view(), name='formacaoList'),
   path('formacaoDelete/<int:pk>', FormacaoView.FormacaoDelete, name='formacaoDelete'),
   path('perfilColaborador/<int:pk>', PerfilColaboradorView.as_view(), name='perfilColaborador'),
]