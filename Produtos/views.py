from django.shortcuts import render
from .models import Obra

# Create your views here.


def index(request):
    filmes = Obra.objects.filter(tipo="F")
    series = Obra.objects.filter(tipo="S")

    context = {
        "filmes": filmes,
        "series": series,
    }

    return render(request, "Produtos/index.html", context)
