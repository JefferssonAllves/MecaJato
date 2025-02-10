function add_carro(){
    container = document.getElementById('form-carro')

    HTML="<br><div class='row'><div class='col-md'><input type='text' placeholder='carro' class='form-control' name='carro'></div><div class='col-md'><input type='text' placeholder='placa' class='form-control' name='placa'></div><div class='col-md'><input type='number' placeholder='ano' class='form-control' name='ano'></div></div>"

    container.innerHTML += HTML
}

function exibir_form(tipo){
    add_cliente = document.getElementById('cadastrar-cliente');
    att_cliente = document.getElementById('atualizar-cliente');

    if(tipo == "1"){
        add_cliente.style.display = "block";
        att_cliente.style.display = "none";
    }else{
        add_cliente.style.display = "none";
        att_cliente.style.display = "block";
    }
}

function dados_cliente(){
    //ESCOLHA DO SELECT - RETORNA O ID DO CLIENTE
    cliente = document.getElementById('cliente-select')
    id_cliente = cliente.value
    document.getElementById('id').value = id_cliente

    if (id_cliente != ''){
        csrf_token = document.querySelector('[name=csrfmiddlewaretoken]')

        data = new FormData()
        data.append('id_cliente', id_cliente)


        fetch("/clientes/atualiza_cliente/",{
            method: "POST",
            headers: {
                'X-CSRFToken': csrf_token.value,          
            },
            body: data
        }).then(function(result){
            return result.json()
        }).then(function(data){
            document.getElementById('form-att-cliente').style.display = 'block'

            document.getElementById('nome').value = data['cliente']['nome']
            document.getElementById('sobrenome').value = data['cliente']['sobrenome']
            document.getElementById('email').value = data['cliente']['email']
            document.getElementById('cpf').value = data['cliente']['cpf']

            container_carros = document.getElementById('carros')
            container_carros.innerHTML = ""
            for(i=0; i<data['carros'].length; i++){
                container_carros.innerHTML += "<form action='/clientes/update_carro/"+ data['carros'][i]['id'] +"' method='POST'>\
                        <div class='row'>\
                            <div class='col-md'>\
                                <input type='text' class='form-control' name='carro' value='"+data['carros'][i]['fields']['carro']+"'>\
                            </div>\
                            <div class='col-md'>\
                                <input type='text' class='form-control' name='placa' value='"+data['carros'][i]['fields']['placa']+"'>\
                            </div>\
                            <div class='col-md'>\
                                <input type='number' class='form-control' name='ano' value='"+data['carros'][i]['fields']['ano']+"'>\
                            </div>\
                            <div class='col-md'>\
                                <input type='submit' class='btn btn-success' value='Salvar'>\
                            </div>\
                            </form >\
                            <div class='col-md'>\
                                <a class='btn btn-danger' href='/clientes/excluir_carro/"+ data['carros'][i]['id'] +"'>Excluir</a>\
                            </div>\
                        </div>\
                        <br>"
            }
        })
    }else{
        document.getElementById('form-att-cliente').style.display = 'none'
    }

}
function update_cliente(){
    id = document.getElementById('id').value
    nome = document.getElementById('nome').value
    sobrenome = document.getElementById('sobrenome').value
    email = document.getElementById('email').value
    cpf = document.getElementById('cpf').value

    fetch('/clientes/update_cliente/'+ id, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token.value,  
        },
        body: JSON.stringify({
            nome: nome,
            sobrenome: sobrenome,
            email: email,
            cpf: cpf,
        })
    }).then(function(result){
        return result.json()
    }).then(function(data){

        if(data['status'] == 200){
            console.log('ATUALIZADO COM SUCESSO')
        }else{
            console.log('ALGO DEU ERRADO')
        }
    })
}
function mascaraCPF(input) {
    var valor = input.value;
  
    // Remove todos os caracteres que não são números
    valor = valor.replace(/\D/g, "");
  
    // Adiciona pontos e traço na posição correta
    valor = valor.replace(/(\d{3})(\d)/, "$1.$2");
    valor = valor.replace(/(\d{3})(\d)/, "$1.$2");
    valor = valor.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
  
    input.value = valor;
}