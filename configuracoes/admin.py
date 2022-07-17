from django.contrib import admin
from .models import Configuracao


class ConfiguracaoAdmin(admin.ModelAdmin):
    list_display= (
        'valor_hora','valor_mes'
    )

admin.site.register(Configuracao, ConfiguracaoAdmin)