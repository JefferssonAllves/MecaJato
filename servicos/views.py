from django.shortcuts import render, redirect
from django.http import HttpResponse
from clientes.models import Cliente
from .models import CategoriaManutencao
# Create your views here.
def novo_servico(request):
    lista_clientes = Cliente.objects.all()
    return render(request, './novo_servico.html', {'clientes': lista_clientes})

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
        
        return redirect('novo_servico')