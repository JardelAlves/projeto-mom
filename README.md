# Projeto MOM: Middleware Orientado a Mensagem
> Projeto para implementar um sistema de gerenciamento e utilização de comunicação por mensagens utilizando Python e RabbitMQ.
## Instalação
Instale o Pyro4, Pygame, Pygame GUI e RabbitMQ:
#### Pyro4
´´´
pip install Pyro4
´´´
#### Pygame
´´´
pip install pygame
´´´
#### Pygame GUI
´´´
pip install pygame-gui
´´´
#### RabbitMQ
Instale o RabbitMQ através do **chocolatey**. Para mais detalhes, [clique no link](https://www.rabbitmq.com/download.html)

## Execução
Execute o comando para iniciar o servidor de nomes:
´´´
python -m Pyro4.naming
´´´
Execute o servidor do chat:
´´´
python \\.server.py
´´´
Execute o chat:
´´´
python \\.chat.py
´´´

## Observações
1. O servidor possui um limite de até 8 jogadores.