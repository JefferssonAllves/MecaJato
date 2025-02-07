from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Carro
from django.http import HttpResponse, JsonResponse
import re
from django.core import serializers #TRANSFORMA UM OBJETO DE MODELS EM UM FORMATO JSON COM O TIPO STRING
import json #TRANSFOMRA A STRING QUE VEIO DO serializar PARA O TIPO JSON
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse



def clientes(request):
    if request.method == 'GET':
        lista_clientes = Cliente.objects.all()
        return render(request, './clientes.html', {'clientes':lista_clientes})
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')
        
        
        cliente = Cliente.objects.filter(cpf=cpf)
        lista_carros = zip(carros, placas, anos)
        
        if cliente.exists(): #TODO EVITA SALVAR CLIENTES QUE JA ESTAO CADASTRADOS
            return render(request,'./clientes.html', {'nome':nome, 'sobrenome':sobrenome, 'email':email, 'carros':lista_carros})
        
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email): #TODO TESTA PARA SABER SE O EMAIL FOI ESCRITO DE FORMA CORRETA
            return render(request,'./clientes.html', {'nome':nome, 'sobrenome':sobrenome, 'cpf':cpf, 'carros':lista_carros})

        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )
        cliente.save()
        
        for carro, placa, ano in lista_carros:
            car = Carro(carro=carro, placa=placa, ano=ano, cliente=cliente)
            car.save()
        
        return HttpResponse('Adicionado com sucesso')
        
def att_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    cliente = Cliente.objects.filter(id=id_cliente)
    carros = Carro.objects.filter(cliente=id_cliente)
    
    cliente_json = json.loads(serializers.serialize('json', cliente))[0]['fields'] #TODO TRANSFORMAR O OBJECTO CLIENTE EM UM TIPO DE DADO DO TIPO JSON PARA FACILITAR A RESPOSTA DA REQUISIÇAO
    carros_json = json.loads(serializers.serialize('json', carros))
    carros_json = [{'fields': carro['fields'], 'id': carro['pk']} for carro in carros_json]
    
    data = {'cliente': cliente_json, 'carros': carros_json}
    return JsonResponse(data)

def update_cliente(request, id):
    body = json.loads(request.body)

    nome = body['nome']
    sobrenome = body['sobrenome']
    email = body['email']
    cpf = body['cpf']
    
    cliente =get_object_or_404(Cliente, id=id)
    try:
        cliente.nome = nome
        cliente.sobrenome = sobrenome
        cliente.email = email
        cliente.cpf = cpf
        
        cliente.save()
        return JsonResponse({'status': 200, 'nome': nome, 'sobrenome': sobrenome, 'email': email, 'cpf': cpf})
    
    except:
        return JsonResponse({'status': 500})
    
    
@csrf_exempt
def update_carro(request, id):
    nome_carro = request.POST.get('carro')
    placa = request.POST.get('placa')
    ano = request.POST.get('ano')
    
    carro = Carro.objects.get(id=id)
    lista_carros = Carro.objects.filter(placa=placa).exclude(id=id)

    if lista_carros.exists():
        return HttpResponse('ESSE CARRO JA EXISTE')
    
    
    carro.carro = nome_carro
    carro.placa = placa
    carro.ano = ano
    carro.save()
    return HttpResponse('ATUALIZADO COM SUCESSO')
    
def excluir_carro(request, id):
    try:
        carro = Carro.objects.get(id=id)
        carro.delete()
        return redirect(reverse('clientes')+f'?aba=att_cliente&id_cliente={id}')
    except:
        #TODO EXIBIR MENSAGEM DE ERRO
        return redirect(reverse('clientes')+f'?aba=att_cliente&id_cliente={id}')