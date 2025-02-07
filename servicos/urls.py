
from django.urls import path
from . import views

urlpatterns = [
    path('novo_servico/', views.novo_servico, name='novo_servico'),
    path('adicionar_categoria/', views.adicionar_categoria, name='adicionar_categoria'),
    
]
