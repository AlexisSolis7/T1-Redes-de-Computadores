import socket
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)  # TCP
serverSocket.bind(('192.168.3.94', serverPort))
serverSocket.listen(1)  # Espera cliente

print("Servidor TCP aguardando conexão...")
connectionSocket, clientAddress = serverSocket.accept()
print(f"Conexão estabelecida com {clientAddress}")

for i in range(10):
    message = connectionSocket.recv(2048)  # Recebe ping
    if not message:
        break

    print(f"Recebido: {message.decode()}")

    modifiedMessage = message.decode().upper()
    connectionSocket.send(modifiedMessage.encode())  # Envia pong

connectionSocket.close()
serverSocket.close()
