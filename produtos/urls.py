from django.urls import path
from .views import adiciona_produto, edita_produto, home, home_produtos,entrada_saida, tela_adicao_produto, tela_edicao_produto

namespace = 'produtos'

urlpatterns = [
    path('', home, name="home"),
    path('produtos/', home_produtos, name="home_produtos"),
    path('produtos/<uuid:id>/', home_produtos, name="remove_produto"),
    path('produtos/adicionar/salvar/', adiciona_produto, name="adiciona_produto"),
    path('produtos/adicionar', tela_adicao_produto, name="tela_adiciona_produto"),
    path('produtos/alterar/<uuid:id>/', tela_edicao_produto, name="edicao_produto"),
    path('editaprodutos/<uuid:id>/', edita_produto, name="edita_produto"),
    path('entradasaida/', entrada_saida, name="home_entradasaida"),
]

