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
            Q(nome__icontains=query)
        )
        print(obras)

        context = {
            "query": query,
            "obras": obras
        }

    return render(request, "Produtos/index.html", context)


def list_films(request):
    '''View function for films page. Returns all movies.'''

    filmes = Obra.objects.filter(tipo="F")

    context = {
        "filmes": filmes,
    }

    if request.GET.get("q"):
        query = request.GET.get("q")
        obras = Obra.objects.filter(
            Q(nome__icontains=query)
        )
        print(obras)

        context = {
            "query": query,
            "obras": obras
        }

    return render(request, "Produtos/list_films.html", context)


def list_series(request):
    '''View function for series page. Returns all series.'''

    series = Obra.objects.filter(tipo="S")

    context = {
        "series": series,
    }

    if request.GET.get("q"):
        query = request.GET.get("q")
        obras = Obra.objects.filter(
            Q(nome__icontains=query)
        )
        print(obras)

        context = {
            "query": query,
            "obras": obras
        }

    return render(request, "Produtos/list_series.html", context)


def detail(request, id):
    '''View function for detail page. Returns a specific movie or series.'''

    obra = Obra.objects.get(pk=id)

    context = {
        "obra": obra,
    }

    return render(request, "Produtos/detail.html", context)
