from django.contrib import admin
from .models import *

# Register your models here.

class LivrosAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    list_display_links = ('id',)
    search_fields = ('titulo',)

admin.site.register(Livros, LivrosAdmin) 

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')
    list_display_links = ('id',)
    search_fields= ('tipo',)

admin.site.register(Genero, GeneroAdmin)

class LivroGeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_livro', 'fk_genero')
    list_display_links = ('id',)
    search_fields = ('tipo',)

admin.site.register(GeneroLivro, LivroGeneroAdmin)
