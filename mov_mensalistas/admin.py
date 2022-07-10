from django.contrib import admin
from .models import (
    MovMensalista,
)


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display= ('mensalista', 'dt_pgto', 'total')

admin.site.register(MovMensalista,MovMensalistaAdmin)
