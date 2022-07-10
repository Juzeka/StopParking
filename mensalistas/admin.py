from django.contrib import admin
from .models import Mensalista


class MensalistaAdmin(admin.ModelAdmin):
    list_display= ('veiculo','inicio','valor_mes')

admin.site.register(Mensalista, MensalistaAdmin)