from django.db import models

# Create your models here.


class Filme(models.Model):

    nome = models.CharField(max_length=100)
    sinopse = models.TextField()
    elenco = models.TextField()
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    imagem = models.ImageField(upload_to='imagens')
    poster = models.ImageField(upload_to='imagens')
    trailer = models.URLField()

    def __str__(self):
        return self.nome
