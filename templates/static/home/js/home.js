function mostrar_tabela(table){
    ordem_servico = document.getElementById('ordem-servico');
    clientes = document.getElementById('clientes');
    carros = document.getElementById('carros');
    servicos = document.getElementById('servicos');

    console.log('TESTE')
    if(table == '1'){
        ordem_servico.style.display = 'block';
        clientes.style.display = 'none';
        carros.style.display = 'none';
        servicos.style.display = 'none';
    }else if(table == '2'){
        ordem_servico.style.display = 'none';
        clientes.style.display = 'block';
        carros.style.display = 'none';
        servicos.style.display = 'none';
    }else if(table == '3'){
        ordem_servico.style.display = 'none';
        clientes.style.display = 'none';
        carros.style.display = 'block';
        servicos.style.display = 'none';
    }else{
        ordem_servico.style.display = 'none';
        clientes.style.display = 'none';
        carros.style.display = 'none';
        servicos.style.display = 'block';
    }
}

