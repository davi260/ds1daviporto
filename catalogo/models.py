from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=150)
    nacionalidade = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.nome
 
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
class Livro(models.Model):
    categoria =models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE,
        related_name="livros",
    )
    autores = models.ManyToManyField(
        Autor,
        related_name="livros",
    )
    titulo = models.CharField(max_length=200)
    sinopse = models.TextField(blank=True)
    paginas = models.IntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    data_publicacao = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo

class FichaTecnica(models.Model):
    livro = models.OneToOneField(
        Livro,
        on_delete=models.CASCADE,
        related_name="ficha_tecnica",
    )
    isbn = models.CharField(max_length=20, unique=True)
    editora = models.CharField(max_length=100)
    numero_edicao = models.IntegerField(default=1)
    def __str__(self):
        return f"Ficha técnica de {self.livro.titulo}"

# Create your models here.
