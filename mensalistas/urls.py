from django.urls import path
from .views import (
    lista_mensalistas,
    mensalista_novo,
    mensalista_updade,
    mensalista_delete,
)


urlpatterns = [
    path('',lista_mensalistas,name='core_lista_mensalistas'),
    path('novo',mensalista_novo,name='core_mensalista_novo'),
    path('update/<int:id>',mensalista_updade,name='core_mensalista_update'),
    path('delete/<int:id>',mensalista_delete,name='core_mensalista_delete'),
]
