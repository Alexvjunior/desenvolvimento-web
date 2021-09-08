from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)

    user = models.OneToOneField(
        to=User,
        on_delete=models.PROTECT,
        default=None,
    )

    departamentos = models.ManyToManyField(to=Departamento)

    empresa = models.ForeignKey(
        to=Empresa, on_delete=models.PROTECT,
        default=None,
    )

    def __str__(self) -> str:
        return self.nome
