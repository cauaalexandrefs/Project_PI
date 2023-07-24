from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Filme

# Create your views here.


def index(request):
    '''View function for home page. Returns all movies.'''

    filmes = Filme.objects.all()

    context = {
        "filmes": filmes,
    }

    if request.GET.get("q"):
        query = request.GET.get("q")
        results = Filme.objects.filter(
            Q(nome__icontains=query)
        )

        context["query"] = query
        context["results"] = results

    return render(request, "Produtos/index.html", context)


def detail(request, id):
    '''View function for detail page. Returns a specific movie .'''

    filme = Filme.objects.get(pk=id)
    filmes = Filme.objects.filter(id__lt=5).order_by("-id")
    context = {
        "filme": filme,
        "filmes": filmes,
    }

    return render(request, "Produtos/detail.html", context)


def admin(request):
    '''View function for admin page. Returns all movies.'''

    filmes = Filme.objects.all()

    context = {
        "filmes": filmes,
    }

    return render(request, "Produtos/admin.html", context)


def delete(request, id):
    '''View function for delete a movie.'''

    filme = Filme.objects.get(pk=id)
    filme.delete()

    return redirect("/produtos/admin")
