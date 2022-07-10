from django import forms
from django.forms import ModelForm
from .models import *


class VeiculoForm(ModelForm):
    class Meta:
        model= Veiculo
        fields = '__all__'
