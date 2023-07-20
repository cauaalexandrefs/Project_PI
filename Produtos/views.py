from django.shortcuts import render
from django.db.models import Q
from .models import Obra

# Create your views here.


def index(request):
    '''View function for home page. Returns all movies and series.'''

    filmes = Obra.objects.filter(tipo="F")
    series = Obra.objects.filter(tipo="S")

    context = {
        "filmes": filmes,
        "series": series,
    }

    if request.GET.get("q"):
        query = request.GET.get("q")
        obras = Obra.objects.filter(
            Q(nome__icontains=query) | Q(tipo__icontains=query) 
        )
        print(obras)

        context = {
            "query": query,
            "obras": obras
        }

    return render(request, "Produtos/index.html", context)


def detail(request, id):
    '''View function for detail page. Returns a specific movie or series.'''

    obra = Obra.objects.get(pk=id)

    context = {
        "obra": obra,
    }

    return render(request, "Produtos/detail.html", context)
