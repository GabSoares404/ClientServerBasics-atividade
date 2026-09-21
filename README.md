# ClientServerBasics (2.0)

Este projeto implementa um sistema básico de cliente-servidor usando sockets TCP em Python. O servidor fornece funcionalidades de processamento de texto que podem ser requisitadas remotamente pelo cliente.

## O que o sistema faz
O sistema consiste em um servidor que aguarda conexões e um cliente que se conecta a ele. O servidor é capaz de receber mensagens de texto, interpretá-las e executar duas funções distintas:
1. **UPPER**: Converte todo o texto recebido para letras maiúsculas.
2. **REVERSE**: Inverte a ordem dos caracteres do texto recebido.

O cliente conecta-se ao servidor e, na mesma sessão (sem fechar a conexão), faz múltiplas requisições demonstrando ambas as funcionalidades.

## Protocolo de Comunicação
O protocolo de comunicação baseia-se no envio de uma string pelo cliente ao servidor. A string deve seguir o seguinte formato:
`COMANDO texto_para_processar`

- `COMANDO`: Deve ser uma das operações suportadas pelo servidor (`UPPER` ou `REVERSE`).
- `texto_para_processar`: O dado em si que o servidor irá processar.
- Eles devem ser separados por um espaço.

Exemplo de requisição:
`UPPER ola mundo`
O servidor processa e responde com:
`OLA MUNDO`

Exemplo de requisição:
`REVERSE ola mundo`
O servidor processa e responde com:
`odnum alo`

## Como executar

1. Abra um terminal e inicie o servidor executando o seguinte comando:
   ```bash
   python server.py
   ```
   O servidor começará a rodar e a aguardar por conexões na porta 50000.

2. Em um **segundo terminal**, execute o cliente com o comando:
   ```bash
   python client.py
   ```
   O cliente se conectará ao servidor, enviará as requisições de teste e imprimirá as respostas recebidas na tela.
