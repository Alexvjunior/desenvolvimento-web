from django.contrib import admin
from .models import ContatoModel

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_filter = ('categoria',)

admin.site.register(ContatoModel, ContatoAdmin)
