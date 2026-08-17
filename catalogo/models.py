from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    sinopse = models.TextField(blank=True)
    paginas = models.IntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    data_publicacao = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo

# Create your models here.
