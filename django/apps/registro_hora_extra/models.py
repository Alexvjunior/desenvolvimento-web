from django.db import models
from apps.funcionarios.models import Funcionario

class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(
        to=Funcionario,
        on_delete=models.PROTECT,
        default=None,
    )

    def __str__(self) -> str:
        return self.motivo