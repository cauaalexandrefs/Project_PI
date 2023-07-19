from django.db import models

# Create your models here.

class Produto(models.Model):

    sabor = models.CharField(max_length=100)
    ingredientes = models.TextField()
    preco = models.DecimalField (decimal_places=2, max_digits=10)
    imagem = models.ImageField (upload_to='imagens')
    

    def __str__(self):
        return "Bolo de " + self.sabor
