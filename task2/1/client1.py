from socket import *

serverIp = 'localhost'
serverPort = 1183

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIp, serverPort))

receivedData = clientSocket.recv(1200).decode()
print(receivedData)

sentData = input('')
clientSocket.send(sentData.encode())

print(clientSocket.recv(1200).decode())
print(clientSocket.recv(1200).decode())

clientSocket.close()
