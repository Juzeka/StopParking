from django.urls import path
from .views import (
    lista_mov_rotativos,
    mov_rotativo_novo,
    mov_rotativo_update,
    mov_rotativo_delete,
)


urlpatterns = [
    path('', lista_mov_rotativos, name='core_lista_mov_rotativos'),
    path('novo', mov_rotativo_novo, name='core_mov_rotativo_novo'),
    path('update/<int:id>', mov_rotativo_update, name='core_mov_rotativo_update'),
    path('delete/<int:id>', mov_rotativo_delete, name='core_mov_rotativo_delete'),
]