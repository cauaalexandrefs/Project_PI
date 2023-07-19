from django.shortcuts import render
from .models import Produto

# Create your views here.

def produto_listar(request):
    produtos = Produto.objects.all()
    context = {
        'produtos':produtos
    }
    return render(request, "Produtos/index.html", context)