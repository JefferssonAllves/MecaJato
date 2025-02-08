from django.db import models
from clientes.models import Cliente, Carro
from datetime import datetime
from secrets import token_hex

# Create your models here.
class CategoriaManutencao(models.Model):
    titulo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.titulo
class Servico(models.Model):
    titulo = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    carro_cliente = models.ForeignKey(Carro, on_delete=models.SET_NULL, null=True)
    data_inicio = models.DateField(null=True)
    data_entrega = models.DateField(null=True)
    total_pedido = models.DecimalField(max_digits=8, decimal_places=2)
    finalizado = models.BooleanField(default=False)
    protocolo = models.CharField(max_length=52, null=True,  blank=True)
