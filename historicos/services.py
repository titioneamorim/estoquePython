from historicos.models import HistoricoModel
from django.shortcuts import render
from produtos.services import ProdutoServices

produtoServices = ProdutoServices()

class HistoricoServices():

    def buscar_todos_historicos(self) -> list[HistoricoModel]:
        return HistoricoModel.objects.all()
    
    