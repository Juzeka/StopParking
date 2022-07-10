from django.contrib import admin
from .models import (
    MovMensalista,
)


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display= ('mensalista', 'pago_em', 'valor_pago')

admin.site.register(MovMensalista,MovMensalistaAdmin)
