from django.shortcuts import render
from clientes.models import Cliente, Carro
from servicos.models import Servico, CategoriaManutencao
# Create your views here.
def home(request):
    clientes = Cliente.objects.all()
    carros = Carro.objects.all()
    ordem_servicos = Servico.objects.all()
    categoria_manutencao = CategoriaManutencao.objects.all()
    return render(request, './home.html', {'clientes': clientes, 'carros': carros, 'ordem_servicos': ordem_servicos, 'categoria_manutencao': categoria_manutencao})