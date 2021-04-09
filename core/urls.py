from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import (
    home,
    lista_pessoas,
    lista_veiculos,
    lista_mov_rotativos,
    lista_mensalistas,
    lista_mov_mensalistas,
    pessoa_novo,
    veiculo_novo,
    mov_rotativo_novo,
    mensalista_novo,
    mov_mensalista_novo,
    pessoa_update,
    veiculo_update,
    mov_rotativo_update,
    mensalista_updade,
    mov_mensalista_update,
    pessoa_delete,
    veiculo_delete,
    mov_rotativo_delete,
    mensalista_delete,
    mov_mensalista_delete,
 

)

urlpatterns = [
    path('',home, name= 'core_home'),
    path('pessoas',lista_pessoas, name= 'core_lista_pessoas'),
    path('pessoa_novo',pessoa_novo, name= 'core_pessoa_novo'),
    path('pessoa_update/<int:id>',pessoa_update, name= 'core_pessoa_update'),
    path('pessoa_delete/<int:id>',pessoa_delete, name= 'core_pessoa_delete'),

    path('veiculos', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo_novo', veiculo_novo, name='core_veiculo_novo'),
    path('veiculo_update/<int:id>', veiculo_update, name='core_veiculo_update'),
    path('veiculo_delete/<int:id>', veiculo_delete, name='core_veiculo_delete'),

    path('mov_rotativos', lista_mov_rotativos, name='core_lista_mov_rotativos'),
    path('mov_rotativo_novo', mov_rotativo_novo, name='core_mov_rotativo_novo'),
    path('mov_rotativo_update/<int:id>', mov_rotativo_update, name='core_mov_rotativo_update'),
    path('mov_rotativo_delete/<int:id>', mov_rotativo_delete, name='core_mov_rotativo_delete'),

    path('mensalistas',lista_mensalistas,name='core_lista_mensalistas'),
    path('mensalista_novo',mensalista_novo,name='core_mensalista_novo'),
    path('mensalista_update/<int:id>',mensalista_updade,name='core_mensalista_update'),
    path('mensalista_delete/<int:id>',mensalista_delete,name='core_mensalista_delete'),

    path('mov_mensalistas',lista_mov_mensalistas, name='core_lista_mov_mensalistas'),
    path('mov_mensalista_novo',mov_mensalista_novo, name='core_mov_mensalista_novo'),
    path('mov_mensalista_update/<int:id>',mov_mensalista_update, name='core_mov_mensalista_update'),
    path('mov_mensalista_delete/<int:id>',mov_mensalista_delete, name='core_mov_mensalista_delete'),
]
