from django.contrib import admin

from .models import (
    Pessoa,
    Paramentro,
)


admin.site.register(Pessoa)
admin.site.register(Paramentro)
