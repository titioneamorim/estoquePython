import uuid
from .models import ProdutoModel
from .serializers import ProdutoSerializer
from django.db.models import Q, Value

class ProdutoServices():
    
    def buscar_todos_produtos(self) -> list[ProdutoModel]:
        return ProdutoModel.objects.all()

    def buscar_produto_por_id(self, id:uuid) -> ProdutoModel:
        return ProdutoModel. objects.filter(id=id).first()
    
    def buscar_produto_por_codigo(self, codigo:str) -> ProdutoModel:
        return ProdutoModel.objects.filter(codigo=codigo).first()

    def buscar_produto_por_termo(self, termo:str) -> list[ProdutoModel]:
        return ProdutoModel.objects.filter( Q(nome__icontains=termo) | Q(codigo__icontains=termo))
        
    def remover_produto_by_id(self, id:uuid) -> int:
        return ProdutoModel.objects.filter(id=id).delete()

    def editar_produto(self, produto:ProdutoModel, data:dict) -> None:
        produto.nome = data['nome']
        produto.codigo = data['codigo']
        try:
            produto.save()
        except Exception as e:
            return e.args

    def consultar_por_cod_produto(self, codigo:str) -> bool:
        result_query = ProdutoModel.objects.filter(codigo=codigo).first()
        return result_query is not None

    def salvar_produto(self, produto:ProdutoSerializer):
        produto.save()
        
