from django.urls import path, include
from .views import (
    home,
    lista_pessoas,
    pessoa_novo,
    pessoa_update,
    pessoa_delete,
)


urlpatterns = [
    path('',home, name= 'core_home'),
    path('pessoas',lista_pessoas, name= 'core_lista_pessoas'),
    path('pessoa_novo',pessoa_novo, name= 'core_pessoa_novo'),
    path('pessoa_update/<int:id>',pessoa_update, name= 'core_pessoa_update'),
    path('pessoa_delete/<int:id>',pessoa_delete, name= 'core_pessoa_delete'),

    path('veiculo/', include('veiculos.urls')),
    path('mensalista/', include('mensalistas.urls')),
    path('mov_rotativo/', include('mov_rotativos.urls')),
    path('mov_mensalista/', include('mov_mensalistas.urls')),
]
