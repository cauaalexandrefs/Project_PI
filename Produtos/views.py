from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Filme
from .forms import FilmeForm

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


@login_required(login_url="/admin/login/?next=/produtos/admin/")
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


def create(request):
    '''View function for create a movie.'''

    if request.method == "POST":
        Filme.objects.create(
            nome=request.POST.get("nome"),
            descricao=request.POST.get("descricao"),
            preco=request.POST.get("preco"),
            imagem=request.FILES.get("imagem"),
        )

        return redirect("/produtos/admin")

    form = FilmeForm()
    return render(request, "Produtos/create.html", {"form": form})


def update(request, id):
    '''View function for update a movie.'''

    filme = Filme.objects.get(pk=id)

    if request.method == "POST":
        filme.nome = request.POST.get("nome")
        filme.descricao = request.POST.get("descricao")
        filme.preco = request.POST.get("preco")
        filme.imagem = request.FILES.get("imagem")
        filme.save()

        return redirect("/produtos/admin")

    form = FilmeForm(instance=filme)
    return render(request, "Produtos/update.html", {"form": form})
