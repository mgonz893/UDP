#UDPClient.py

from socket import socket, SOCK_DGRAM, AF_INET, timeout as TimeoutException

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')
clientSocket.settimeout(1.0)
# Message is sent to server
clientSocket.sendto(message.encode(), (serverName, serverPort))
try:
    modifiedMessage, addr = clientSocket.recvfrom(2048)
    print(modifiedMessage, addr)
except TimeoutException:
    print("Timeout!\n")
if not message:
# Server modifies the message to all uppercase and returns to client
    print(modifiedMessage, addr)

clientSocket.close()

#Allow the client to give up if no response has been received within 1 second.
#Added timeout on line 9
