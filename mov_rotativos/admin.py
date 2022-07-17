from django.contrib import admin
from .models import (
    MovRotativo,
)


class MovRotativoAdmin(admin.ModelAdmin):
    list_display= (
        'placa', 'checkin', 'checkout','valor_pago', 'pago'
    )

admin.site.register(MovRotativo, MovRotativoAdmin)
