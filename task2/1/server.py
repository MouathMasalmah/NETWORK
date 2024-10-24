from socket import *

serverPort = 1183
serverIp = 'localhost'

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIp, serverPort))
serverSocket.listen(1)
print("Server is on and waiting for a connection...")

while True:
    connectionClient, clientAddress = serverSocket.accept()
    print(f"Connected to {clientAddress}")
    
    connectionClient.send("Enter your message: ".encode())
    clientMessage = connectionClient.recv(1200).decode()
    print("Message from client:", clientMessage)
    
    newMessage = ''.join(['#' if char in vowels else char for char in clientMessage])
    
    connectionClient.send("This is the new message: ".encode())
    connectionClient.send(newMessage.encode())
    
    connectionClient.close()
    print("Connection closed.")
    break
