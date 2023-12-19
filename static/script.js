document.getElementById('comprarBtn').addEventListener('click', function (event) {
    event.preventDefault();

    var nomeInput = document.querySelector('.form-input');
    if (nomeInput.value.trim() === '') {
        alert('Por favor, preencha o campo de nome antes de comprar.');
        return;
    }

    var confirmacao = window.confirm("Tem certeza de que deseja confirmar a compra?");
    if (!confirmacao) {
        return;
    }

    var selectedOption = document.getElementById('action-select').value;
    var message = "Muito obrigado pela sua compra!<br><br>";
    const pix = document.getElementById('codigoPix');
    pix.innerHTML = ''; 

    if (selectedOption === 'pix') {
        message += "<td>Utilize o app do seu banco para ler o QRCode</td>";
        document.getElementById('codigoPix').style.display = 'block';

        var valor = document.getElementById('item-valor').getAttribute('data-item-valor');
        valor = converteInteiro(valor);
        // Carregar a imagem do QR Code apenas quando a opção Pix for selecionada
        fetch(`/gerar_qrcode/${valor}`)
            .then(response => response.text())
            .then(data => {
                // Exibir a imagem no elemento "codigoPix"
                pix.innerHTML = `<img id="qrcode" src="/gerar_qrcode/${valor}" alt="QR Code">`;
            });
    } else if (selectedOption === 'card') {
        message += 'Pagamento no cartão de crédito<br>Preencha os dados';
    } else if (selectedOption === 'doc') {
        conta = '3209193-2';
        agencia = '03928-1';
        nome = 'Nome do Titular';
        message += `Nome do beneficiário: ${nome}<br>Agência: ${agencia}<br>Conta para depósito: ${conta}`
    }

    document.getElementById('popup-message').innerHTML = message;
    document.getElementById('popDiv').style.display = 'block';

    var form = document.getElementById('action-form');
    var formData = new FormData(form);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', form.action, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            document.getElementById('popup-message').innerHTML = "Compra realizada com sucesso!";
        }
    };

    xhr.send(formData);
});


// function pop(div) {
//     document.getElementById(div).style.display = 'block';
// }

function hide(div) {
    document.getElementById(div).style.display = 'none';
    window.location.href = '/'
}
//Sair apertando ESC
document.onkeydown = function (evt) {
    evt = evt || window.event;
    if (evt.keyCode == 27) {
        hide('popDiv');
    }
};


function converteInteiro(valor) {
    var match = valor.match(/R\$\s*(\d+)/);

    if (match && match[1]) {
        var inteiro = parseInt(match[1], 10); // Converte a correspondência para um número inteiro
        return inteiro
    }
}
