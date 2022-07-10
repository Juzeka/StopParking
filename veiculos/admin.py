from django.contrib import admin

from .models import (
    Marca,
    Veiculo,
)

admin.site.register(Marca)
admin.site.register(Veiculo)
