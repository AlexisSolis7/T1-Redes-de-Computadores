import socket
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)  # UDP
serverSocket.bind(('192.168.3.94', serverPort))  # Escutando nessa porta

print("O servidor está recebendo mensagens...")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)  # Recebe ping
    print(f"Recebido de {clientAddress}: {message.decode()}")

    modifiedMessage = message.decode().upper()  # Modifica para resposta tipo pong
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)  # Envia pong
