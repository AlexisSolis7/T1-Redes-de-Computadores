import socket
import time
from socket import *

serverName = '192.168.3.94'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)  # TCP
clientSocket.connect((serverName, serverPort))  # Conecta com o servidor

for i in range(10):
    message = f"ping {i+1}"
    sendTime = time.time()

    try:
        clientSocket.send(message.encode())  # Envia ping
        modifiedMessage = clientSocket.recv(2048)  # Recebe pong
        receiveTime = time.time()

        rtt = receiveTime - sendTime
        print(f"Recebido: {modifiedMessage.decode()} | RTT = {rtt:.4f} segundos")

    except Exception as e:
        print(f"Erro na comunicação: {e}")

    time.sleep(1)

clientSocket.close()  # Fecha conexão
