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
function dados_cliente(){
    cliente_select = document.getElementById('id-cliente')
    id_cliente = cliente_select.value

    if(id_cliente != ''){
        csrf_token = document.querySelector('[name=csrfmiddlewaretoken]')

        data = new FormData()
        data.append('id_cliente', id_cliente)

        fetch("/servicos/carro_cliente/",{
            method: "POST",
            headers: {
                'X-CSRFToken': csrf_token.value,          
            },
            body: data
        }).then(function(result){
            return result.json()
        }).then(function(data){
            carro_select = document.getElementById('carro-select')
            for(i=0; i<data['carros'].length; i++){
                nova_opcao = document.createElement('option')
                nova_opcao.value = data['carros'][i]['id']
                nova_opcao.text = data['carros'][i]['fields']['carro']
                carro_select.add(nova_opcao)
            }
        })
    }
}
function att_preco(){
    select = document.getElementById('select-manutencao');
    valor_total = document.getElementById('valor-total');

    preco_selecionados = Array.from(select.selectedOptions).map(option => option.value);
    preco_total = 0
    for(i=0; i<preco_selecionados.length; i++){
        preco_total += parseFloat(preco_selecionados[i])
    }
    preco_total = "TOTAL: R$" + preco_total
    valor_total.innerHTML = preco_total
}