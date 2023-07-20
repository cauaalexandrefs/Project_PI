from django.db import models

# Create your models here.


class Obra(models.Model):

    CATEGORIA_CHOICES = (
        ("F", "Filme"),
        ("S", "Série"),
    )

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=CATEGORIA_CHOICES)
    sinopse = models.TextField()
    elenco = models.TextField()
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    imagem = models.ImageField(upload_to='imagens')

    def __str__(self):
        return self.nome
