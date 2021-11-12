from historicos.models import HistoricoModel
from django.shortcuts import render
from produtos.services import ProdutoServices
from django.db.models import Q, Value

produtoServices = ProdutoServices()

class HistoricoServices():

    def buscar_todos_historicos(self) -> list[HistoricoModel]:
        return HistoricoModel.objects.all()
    
    def buscar_historico_by_termo(self, termo:str):
        return HistoricoModel.objects.filter( Q(funcionario__icontains=termo) | Q(descricao__icontains=termo) | Q(tipo__icontains=termo))