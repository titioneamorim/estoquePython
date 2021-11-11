import uuid
from django import db
from django.db import models
from django_extensions.db.models import TimeStampedModel

from produtos.models import ProdutoModel

class HistoricoModel(TimeStampedModel):
    id = models.UUIDField(
        db_column='ID',
        primary_key=True,
        unique=True,
        editable=False,
        default= uuid.uuid4
    )

    produto_id = models.ForeignKey(
        ProdutoModel,
        on_delete=models.CASCADE
    )

    data_entrada = models.DateField(auto_now=True)

    funcionario = models.CharField(max_length=50)

    tipo= models.CharField(max_length=7)

    descricao = models.TextField()

    quantidade = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = 'HISTORICO'
        verbose_name = 'Historico'
        verbose_name_plural = 'Historicos'

