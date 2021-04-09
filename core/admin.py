from django.contrib import admin

from .models import (
    Marca,
    Veiculo,
    Pessoa,
    Paramentro,
    MovRotativo,
    Mensalista,
    MovMensalista,
)
class MovRotativoAdmin(admin.ModelAdmin):
    list_display= ('checkin','checkout','valor_hora','veiculo','pago','horas_total')

class MensalistaAdmin(admin.ModelAdmin):
    list_display= ('veiculo','inicio','valor_mes')

class MovMensalistaAdmin(admin.ModelAdmin):
    list_display= ('mensalista', 'dt_pgto', 'total')

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Paramentro)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Mensalista, MensalistaAdmin)
admin.site.register(MovMensalista,MovMensalistaAdmin)