import socket
import time
from socket import *

serverName = '192.168.3.94'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)  # UDP
clientSocket.settimeout(1)  # Espera no máximo 1s pela resposta

for i in range(10):
    message = f"ping {i+1}"
    sendTime = time.time()

    try:
        clientSocket.sendto(message.encode(), (serverName, serverPort))  # Envia ping
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)     # Espera pong
        receiveTime = time.time()

        rtt = receiveTime - sendTime  # Calcula RTT
        print(f"Recebido: {modifiedMessage.decode()} | RTT = {rtt:.4f} segundos")

    except timeout:
        print(f"Pacote {i+1} perdido (timeout de 1s)")  # Perda de pacote

    time.sleep(1)

clientSocket.close()  # Fecha conexão
