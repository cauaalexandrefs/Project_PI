from django.shortcuts import redirect, render, get_object_or_404
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
    filmes = Filme.objects.filter(id__lt=20).order_by("-id")
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
        form = FilmeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        else:
            print(form.errors)

        return redirect("/produtos/admin")

    form = FilmeForm()
    return render(request, "Produtos/form.html", {"form": form})


def update(request, id):
    filme = get_object_or_404(Filme, pk=id)

    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('/produtos/admin')

    form = FilmeForm(instance=filme)

    return render(request, 'Produtos/form.html', {'form': form})
