from django.forms import ModelForm
from .models import MovMensalista


class MovMensalistaForm(ModelForm):
    class Meta:
        model= MovMensalista
        fields = '__all__'