from django.db import models

# Create your models here.

class Produto(models.Model):

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    marca = models.CharField(max_length=100)
    preco = models.DecimalField (decimal_places=2, max_digits=10)
    imagem = models.ImageField (upload_to='imagens')
    

    def __str__(self):
        return self.nome + " - " + self.marca
