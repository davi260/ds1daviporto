from django.contrib import admin
from .models import Categoria, Livro
# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'preco', 'disponivel', 'data_publicacao')
    list_filter = ('disponivel',)
    search_fields = ('titulo',)