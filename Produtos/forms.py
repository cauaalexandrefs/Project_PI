from django.forms import ModelForm
from django import forms
from .models import Filme


class FilmeForm(ModelForm):

    class Meta:
        model = Filme
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sinopse': forms.Textarea(attrs={'class': 'form-control'}),
            'elenco': forms.Textarea(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'trailer': forms.URLInput(attrs={'class': 'form-control'}),
        }
