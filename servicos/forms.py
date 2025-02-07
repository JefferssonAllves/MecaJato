
from django.forms import ModelForm
from .models import Servico, CategoriaManutencao

class FormServico(ModelForm):
    class Meta:
        model = Servico
        fields = ['titulo', 'cliente', 'categoria_manutencao', 'data_inicio', 'data_entrega']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})
            
            