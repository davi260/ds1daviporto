from django.contrib import admin
from .models import Categoria, Livro, Autor, FichaTecnica
class FichaTecnicaInline(admin.StackedInline):
 model = FichaTecnica
 can_delete = False
 extra = 0
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
 list_display = ("titulo", "categoria")
 inlines = [FichaTecnicaInline]
admin.site.register(Categoria)
admin.site.register(Autor)