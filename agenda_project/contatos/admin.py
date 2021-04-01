from django.contrib import admin
from .models import Categoria, Contato
# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
	list_display = ('id', 'nome', 'sobrenome', 'data_criacao', 'telefone', 'mostra')
	list_display_links = ('id', 'nome', 'sobrenome')
	list_per_page = 10
	search_fields = ('nome', 'sobrenome')
	
	list_editable = ['mostra', 'telefone']



class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('id', 'nome')
	list_per_page = 10

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Contato, ContatoAdmin)
