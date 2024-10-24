from socket import *

# Define client parameters
serverIp = 'localhost'
serverPort = 1833

# Create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Communication loop
while True:
    message = input("Enter message to send to server: ")
    clientSocket.sendto(message.encode(), (serverIp, serverPort))
    
    # Receive the server's response
    serverMessage, serverAddress = clientSocket.recvfrom(1200)
    print("Message from server:", serverMessage.decode())
