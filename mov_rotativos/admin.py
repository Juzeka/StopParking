from django.contrib import admin
from .models import (
    MovRotativo,
)


class MovRotativoAdmin(admin.ModelAdmin):
    list_display= (
        'checkin','checkout','valor_hora',
        'veiculo','pago','horas_total'
    )

admin.site.register(MovRotativo, MovRotativoAdmin)
