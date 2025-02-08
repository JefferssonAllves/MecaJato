from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from clientes.models import Cliente, Carro
from .models import CategoriaManutencao
import json
from django.core import serializers




# Create your views here.
def novo_servico(request):
    lista_clientes = Cliente.objects.all()
    lista_manutencoes = CategoriaManutencao.objects.all()
    
    return render(request, './novo_servico.html', {'clientes': lista_clientes, 'manutencoes': lista_manutencoes})

def adicionar_categoria(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo_servico')
        preco = request.POST.get('preco_servico')
        
        print(titulo, preco)
        categoria = CategoriaManutencao(
            titulo = titulo,
            preco = preco  
        )
        
        categoria.save()
        
        return redirect('novo_servico')#TODO ARRUMAR ESSA GAMBIARRA AQUI

        
def carro_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    carros = Carro.objects.filter(cliente=id_cliente)

    carros_json = json.loads(serializers.serialize('json', carros))
    carros_json = [{'id': carro['pk'], 'fields': carro['fields'] } for carro in carros_json]
    data = {'carros': carros_json}

    return JsonResponse(data)