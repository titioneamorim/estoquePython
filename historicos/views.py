from django.shortcuts import render
import uuid
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from rest_framework import serializers
from historicos.serializers import HistoricoSerializer
from historicos.services import HistoricoServices
from django.core.paginator import Paginator

from produtos.services import ProdutoServices

# Create your views here.


_SERVICE = HistoricoServices()
_PROD_SERVICE = ProdutoServices()



def home_historico(request):
    historicos = _SERVICE.buscar_todos_historicos()
    page = request.GET.get('p')
    paginator = Paginator(historicos, 5)
    historicos = paginator.get_page(page)
    produtos = _PROD_SERVICE.buscar_todos_produtos()
    return render(request, 'home_historico.html', context={"historicos":historicos, "produtos":produtos})

def adiciona_historico(request):
    serializer = HistoricoSerializer(data=request.POST)
    if not serializer.is_valid():
        messages.error(request, "Falha ao salvar histórico, verifique os dados.")
        historicos =_SERVICE.buscar_todos_historicos
        produtos = _PROD_SERVICE.buscar_todos_produtos()
        return render(request=request, template_name='home_historico.html', context={"historicos":historicos, "produtos":produtos})
    serializer.save()
    messages.success(request,"Movimentação para o funcionário "+ request.POST.get('funcionario') +" salva com sucesso.")
    return HttpResponseRedirect('/historicos/')

def consulta_historico(request):
    termo = request.GET.get('termo')
    page = request.GET.get('p')
    historicos = _SERVICE.buscar_historico_by_termo(termo)
    paginator = Paginator(historicos, 5)
    historicos = paginator.get_page(page)
    return render(request=request, template_name='home_historico.html', context={'historicos' : historicos})

