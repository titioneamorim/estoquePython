from django.db import models
from django.db.models import fields
from rest_framework.utils import field_mapping
from rest_framework import serializers
from historicos.models import HistoricoModel
from produtos.services import ProdutoServices

SERVICE_PRODUTO = ProdutoServices()

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoModel
        fields = ('id', 'produto_id', 'funcionario', 'tipo', 'descricao', 'quantidade')

    # def create(self, validated_data):
    #     produto = SERVICE_PRODUTO.buscar_produto_por_codigo(validated_data.get('codigo_produto'))
    #     validated_data['produto_id'] = produto.id
    #     return super().create(validated_data)
