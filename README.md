# Presentes Formatura

Pequeno sistema de presentes de uma fomatura.

Com sessão de login para o admin fazer CRUD de presentes, visualizar a lista de presença e mensagens enviadas pelos convidados.

O convidado pode confirmar sua presença no evento, visualizar os presentes simbólicos, deixar uma mensagem e efetuar o pagamento de acordo com o valor do presente escolhido.


### Recursos utilizados

- Python 3.11
- Flask
- SQLITE


## Instalação

Criar ambiente virtual:

``
py -m venv venv
``

Instalar dependências, na pasta raíz do projeto:

``
pip install -r requirements.txt
``


## Execução

Na pasta raíz do projeto, rodar o comando:

``
python main.py
``

A execução em localhost é na porta 5000.

``
http://127.0.0.1:5000
``

Para acessar o modo admin, com as páginas do administrador:
```
http://127.0.0.1:5000/login
usuário: admin
  senha: admin
```


## Estrutura do projeto

```
presentes-formatura
└───instance
│   │   itens_database.db
└───routes
│   │   __init__.py
│   │   compra.py
│   │   item.py
│   │   login.py
|   |   pagamento.py
|   |   presenca.py
└───static
|   └───images
|   │   |  favicon.ico
|   └───styles
|   |   |   mobile.css
|   |   |   style.css
|   |   script.js
└───templates
|   │   adicionar.html
|   │   compras.html
|   |   confirmar.html
|   │   editar.html
|   │   index.html
|   │   itens.html
|   │   layout.html
|   |   lista.html
|   │   login.html
|   │   payment.html
|   │   presenca.html
|   .gitignore
|   config.py
|   main.py
|   models.py
|   README.md
|   requirements.txt
```
