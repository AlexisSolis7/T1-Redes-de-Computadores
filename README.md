# T1-Redes-de-Computadores
# Comunicação Cliente-Servidor com sockets em Python

## Objetivo do Problema
O objetivo do trabalho é desenvolver uma aplicação de comunicação entre cliente e servidor que funcione utilizando o protocolo UDP e analisar as modificações necessárias para que o mesmo sistema funcione utilizando o protocolo TCP. Essa atividade visa consolidar o entendimento prático dos dois principais protocolos da camada de transporte na arquitetura TCP/IP, explorando suas características, vantagens, desvantagens e aplicabilidades.

  ## Conceito
### Protocolo UDP (User Datagram Protocol)
O UDP é um protocolo de transporte não orientado à conexão, ou seja, não é necessário estabelecer uma conexão antes do envio de dados. 
>	Mais leve e rápido.
>
>	Não confiável, pois não garante a entrega, nem a ordem dos pacotes.


### Protocolo TCP (Transmission Control Protocol)
O TCP é um protocolo orientado à conexão, ou seja, requer que cliente e servidor estabeleçam uma conexão antes da troca de dados. 
>	Confiável, pois garante a entrega dos dados na ordem correta.
>
>	Mais robusto, com mecanismos de controle de fluxo, verificação de erros e retransmissão de pacotes perdidos.

  ## Solução
### Implementação com UDP
Foi desenvolvida uma aplicação simples, composta por dois programas:
#### Servidor UDP:
*	Criação de socket com tipo SOCK_DGRAM.
*	Associação do socket a uma porta específica.
*	Espera por mensagens de clientes utilizando recvfrom().
*	Responde ao cliente com sendto().
  
![Imagem do código de Servidor UDP](https://github.com/AlexisSolis7/T1-Redes-de-Computadores/blob/main/Captura%20de%20tela%202025-05-27%20185624.png)


#### Cliente UDP:
*	Criação de socket SOCK_DGRAM.
*	Envia mensagem ao servidor usando sendto().
*	Recebe resposta com recvfrom().

![Imagem do código de Cliente UDP](https://github.com/AlexisSolis7/T1-Redes-de-Computadores/blob/main/Captura%20de%20tela%202025-05-27%20192942.png)


![Imagem do código de Cliente UDP](https://github.com/AlexisSolis7/T1-Redes-de-Computadores/blob/main/Captura%20de%20tela%202025-05-27%20193403.png) 

  ## Resultado Final
A aplicação com UDP funcionou corretamente:
* O cliente envia mensagens ao servidor;
*	O servidor respondeu adequadamente.

> Servidor:

![Resultado do servidor](https://github.com/AlexisSolis7/T1-Redes-de-Computadores/blob/main/Captura%20de%20tela%202025-06-09%20093254.png)

> Cliente:

![Resultado do Cliente](https://github.com/AlexisSolis7/T1-Redes-de-Computadores/blob/main/Captura%20de%20tela%202025-06-09%20092831.png)


### Adaptação para TCP
Para adaptar a mesma lógica para TCP, as seguintes alterações são necessárias:

> Substituir SOCK_DGRAM por SOCK_STREAM.

#### No servidor:
>	Utilizar listen() para aguardar conexões.
>
>	Utilizar accept() para aceitar uma conexão de um cliente.
>
>	Enviar e receber dados usando send() e recv().
>
#### No cliente:
>	Utilizar connect() para estabelecer a conexão com o servidor.
>
>	Também usar send() e recv() para a comunicação.

## Resultado final
> Servidor

![Resultado do servidor](https://github.com/AlexisSolis7/T1-Redes-de-Computadores/blob/main/Captura%20de%20tela%202025-06-09%20094341.png)

> Cliente

![Resultado do servidor](https://github.com/AlexisSolis7/T1-Redes-de-Computadores/blob/main/Captura%20de%20tela%202025-06-09%20100128.png)




[Mais informação sobre UDP e TCP](https://www.datacamp.com/pt/tutorial/a-complete-guide-to-socket-programming-in-python)
