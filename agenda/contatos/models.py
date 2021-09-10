from django.db import models
from django.utils import timezone
from categoria.models import CategoriaModel

class ContatoModel(models.Model):

    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    data_criacao = models.DateField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(to=CategoriaModel, on_delete=models.DO_NOTHING)
