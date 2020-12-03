# Project API djngo rest TCC

Projeto de TCC onde desenvolvi um sistema de gerenciamento de projetos baseado em conceitos dos Scrum e do Kanban. 


## **Sumario** <br>
* [Features](#Features)
* [Tecnologias](#Tecnologias)
* [Instalação](#Instalação)
* [Rotas da aplicação](#Rotas-da-aplicação)

<hr />

## Features

- [x] Cadastro de usuário
- [x] Implementação do login
- [x] Implementar registro de usuários
- [x] Cadastro de projetos
- [x] Cadastro de listas de tarefas
- [x] Cadastro de tarefas 
- [x] Movimentar listas de tarefas para diferentes ordens (DragInDrop)
- [x] Movimentar as tarefas em direfentes posições e diferentes listas (DragInDrop)

## Tecnologias

* Python 3.8.5 <br>
* Django 3.0.5
* Django rest frmework 3.11

## Instalação
Clone o repositório:

` > git clone https://github.com/mfatima13/project-TCC.git `

Entra na pasta do projeto:

` > cd project-TCC/ `

Crie o ambiente virtual com o seguinte comando:

` > python -m venv venv `

Ativa o ambiente:

no windows:  ` > ./venv/Scripts/activate`

no linux: ` # source venv/bin/activate`

Agora é so baixar as dependências com o seguinte comando:

` > pip install -r ./requirements.txt `

Agora é só rodar o servidor: 

``` > python manage.py runserver ```

## Rotas da aplicação:

* Admin -> `localhost:8000/admin/`

Acesse esse ![arquivo](/Insomnia_2020-12-03.json) de rotas do Insominia para testar as rotas!
