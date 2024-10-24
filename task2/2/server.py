from socket import *
import threading

# Define server parameters
serverPort = 1833  
serverIp = 'localhost'

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverIp, serverPort))
print("Server is on and ready to receive messages...")

# Dictionary to keep track of the last message from each client
clients = {}

def handle_client(clientMessage, clientAddress):
    clientNumber = clients.get(clientAddress, len(clients) + 1)
    clients[clientAddress] = clientNumber
    
    print(f"\nMessage from client {clientNumber}:")
    print(clientMessage.decode())
    
    # Prompt server user to send a message back to the client
    messageToClient = input(f"Enter your message to client {clientNumber}: ")
    serverSocket.sendto(messageToClient.encode(), clientAddress)

while True:
    clientMessage, clientAddress = serverSocket.recvfrom(1200)
    threading.Thread(target=handle_client, args=(clientMessage, clientAddress)).start()
