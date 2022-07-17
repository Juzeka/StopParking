from django.urls import path
from .views import (
    lista_mov_rotativos,
    mov_rotativo_novo,
    mov_rotativo_update,
    mov_rotativo_delete,
    checkin,
    checkout,
    calcular_valor_apagar
)


urlpatterns = [
    path('', lista_mov_rotativos, name='core_lista_mov_rotativos'),
    path('novo', mov_rotativo_novo, name='core_mov_rotativo_novo'),
    path('update/<int:id>', mov_rotativo_update, name='core_mov_rotativo_update'),
    path('delete/<int:id>', mov_rotativo_delete, name='core_mov_rotativo_delete'),
    path('checkin', checkin, name='checkin'),
    path('checkout/<int:id>', checkout, name='checkout'),
    path('calcular/<int:id>', calcular_valor_apagar, name='calcular'),
]