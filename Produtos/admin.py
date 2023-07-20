from django.contrib import admin
from .models import Obra
# Register your models here.


@admin.register(Obra)
class ObraAdmin(admin.ModelAdmin):

    list_display = ('nome', 'tipo', 'preco', 'sinopse', 'elenco')
