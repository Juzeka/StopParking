from django import forms
from django.forms import ModelForm
from .models import *


class MovRotativoForm(ModelForm):
    class Meta:
        model= MovRotativo
        fields = '__all__'

        widgets = {
            'checkin': forms.DateTimeInput(attrs={'class':'form-control', 'type':'datetime-local'}),
            'checkout': forms.DateTimeInput(attrs={'class':'form-control', 'type':'datetime-local'}),
            'valor_hora': forms.NumberInput(attrs={'class':'form-control', 'step':'0.01'}),
        }



class MovRotativoChekinForm(ModelForm):
    class Meta:
        model= MovRotativo
        fields = ('placa', 'checkin')

        widgets = {
            'placa': forms.TextInput(attrs={'class':'form-control'}),
        }


class MovRotativoChekoutForm(ModelForm):
    class Meta:
        model= MovRotativo
        fields = ('checkout', 'valor_pago', 'pago')