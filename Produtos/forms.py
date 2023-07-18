from django.forms import ModelForm
from django import forms
from .models import Produto

class AlunoForm(ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'descricao' : forms.TextInput(attrs={'class': 'form-control' }),
            'marca' : forms.TextInput(attrs={'class': 'form-control' }),
            'preco': forms.DecimalField(attrs={'class': 'form-control' }),
            'imagem': forms.ImageField(attrs={'class': 'form-control' })
        }
