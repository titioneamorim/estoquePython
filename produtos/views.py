import re
import uuid
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from produtos.serializers import ProdutoSerializer
from .services import ProdutoServices
from django.core.paginator import Paginator

_SERVICE = ProdutoServices()

def home(request):
    return render(request, 'home.html')

def home_produtos(request, id=None):
    if (request.method == 'POST' and id!=None):
        _SERVICE.remover_produto_by_id(id)
    produtos = _SERVICE.buscar_todos_produtos()
    page = request.GET.get('p')
    paginator = Paginator(produtos, 5)
    produtos = paginator.get_page(page)
    return render(request, 'homeProdutos.html', context={'produtos':produtos})

def tela_edicao_produto(request, id:uuid):
    produto = _SERVICE.buscar_produto_por_id(id)
    return render(request, 'edicaoProduto.html', context={"produto":produto})

def edita_produto(request, id:uuid):
    produto = _SERVICE.buscar_produto_por_id(id)
    serializer = ProdutoSerializer(produto, request.POST)
    # if (_SERVICE.consultar_por_cod_produto(request.POST.get('codigo'))):
    #     return render(request=request, template_name='edicaoProduto.html', context={"valido":False, "mensagem":"O código " + request.POST.get('codigo') +" de já está cadastrado.", "produto":produto}) 
    # else:
    # message = _SERVICE.editar_produto(produto,request.POST      )
    if not serializer.is_valid():
         messages.error(request, serializer)
    else:
        serializer.save()
        messages.success(request, "Produto "+ request.POST.get('nome') +" alterado com sucesso")    
    return HttpResponseRedirect('/produtos/')
    
def entrada_saida(request):
    return render(request, 'entrada-saida.html')

def tela_adicao_produto(request):
    return render(request=request, template_name='adicionaProduto.html')

def adiciona_produto(request):
    serializer = ProdutoSerializer(data=request.POST)
    if not serializer.is_valid():
        messages.warning(request, "O código " + request.POST.get('codigo') +" de já está cadastrado.")
        return render(request=request, template_name='adicionaProduto.html') 
    serializer.save()
    messages.success(request,"Produto "+ request.POST.get('nome') +" salvo com sucesso.")
    return HttpResponseRedirect('/produtos/')

def busca_produto(request):
    termo = request.GET.get('termo')
    page = request.GET.get('p')
    produtos = _SERVICE.buscar_produto_por_termo(termo)
    paginator = Paginator(produtos, 5)
    produtos = paginator.get_page(page)
    return render(request=request, template_name='homeProdutos.html', context={'produtos' : produtos})

    