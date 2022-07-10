from django.urls import path
from .views import (
    lista_veiculos,
    veiculo_novo,
    veiculo_update,
    veiculo_delete,
)


urlpatterns = [
    path('', lista_veiculos, name='core_lista_veiculos'),
    path('novo', veiculo_novo, name='core_veiculo_novo'),
    path('update/<int:id>', veiculo_update, name='core_veiculo_update'),
    path('delete/<int:id>', veiculo_delete, name='core_veiculo_delete'),
]