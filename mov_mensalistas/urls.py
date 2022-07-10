from django.urls import path
from .views import (
    lista_mov_mensalistas,
    mov_mensalista_novo,
    mov_mensalista_update,
    mov_mensalista_delete,
)

urlpatterns = [
    path('',lista_mov_mensalistas, name='core_lista_mov_mensalistas'),
    path('novo',mov_mensalista_novo, name='core_mov_mensalista_novo'),
    path('update/<int:id>',mov_mensalista_update, name='core_mov_mensalista_update'),
    path('delete/<int:id>',mov_mensalista_delete, name='core_mov_mensalista_delete'),
]
