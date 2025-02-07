function exibir_form(form){
    categoria_servico = document.getElementById('categoria-servico')
    ordem_servico = document.getElementById('ordem-servico')

    if(form == '1'){
        categoria_servico.style.display = 'block';
        ordem_servico.style.display = 'none';

    }else{
        categoria_servico.style.display = 'none';
        ordem_servico.style.display = 'block';
    }
}