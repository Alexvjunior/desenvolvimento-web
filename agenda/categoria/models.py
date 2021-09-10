from django.db import models

class CategoriaModel(models.Model):
    nome = models.CharField(max_length=255)