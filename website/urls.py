from django.urls import path, include
from.views import home, contato,servico,sobre,planos

urlpatterns = [
    path('',home, name='website_home'),
    path('contato',contato, name='website_contato'),
    path('servico',servico, name='website_servico'),
    path('sobre',sobre, name='website_sobre'),
    path('planos',planos, name='website_planos'),
]