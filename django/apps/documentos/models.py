from django.db import models
from django.db.models.expressions import Func
from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    
    descricao = models.CharField(max_length=100)

    pertence = models.ForeignKey(
        to=Funcionario,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )

    def __str__(self) -> str:
        return self.descricao
