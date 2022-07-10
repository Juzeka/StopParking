from django import forms
from django.forms import ModelForm
from .models import *


class MensalistaForm(ModelForm):
    class Meta:
        model= Mensalista
        fields = '__all__'