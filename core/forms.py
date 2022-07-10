from django import forms
from django.forms import ModelForm
from .models import *


class PessoaForm(ModelForm):
    class Meta:
        model= Pessoa
        fields = '__all__'


class VeiculoForm(ModelForm):
    class Meta:
        model= Veiculo
        fields = '__all__'


class MovRotativoForm(ModelForm):
    class Meta:
        model= MovRotativo
        fields = '__all__'

        widgets = {
            'veiculo': forms.Select(attrs={'class':'form-control'}),
            'checkin': forms.DateTimeInput(attrs={'class':'form-control', 'type':'datetime-local'}),
            'checkout': forms.DateTimeInput(attrs={'class':'form-control', 'type':'datetime-local'}),
            'valor_hora': forms.NumberInput(attrs={'class':'form-control', 'step':'0.01'}),
        }


class MensalistaForm(ModelForm):
    class Meta:
        model= Mensalista
        fields = '__all__'


class MovMensalistaForm(ModelForm):
    class Meta:
        model= MovMensalista
        fields = '__all__'