#UDPServer.py

#UDP (SOCK_DGRAM) is a datagram-based protocol. You send one 
#datagram and get one reply and then the connection terminates.
import random, time 
from socket import socket, SOCK_DGRAM, AF_INET

#Create a UDP socket 
#Notice the use of SOCK_DGRAM for UDP packets
#AF_INET is the Internet address family for IPv4
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
serverSocket.settimeout(60)
print("Waiting for connections")
#Until a message is sent from the client, we do not go into this.
while True:
    # Generate a random number to use for dropping packets
    start_time = time.time()
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(2048)
    # Capitalize the message from the client
    print(message, address)
    message = message.upper()
    if rand < 6:
        print("Dropped the packet!\n")
        continue
    # Send message back to client
    timePrint = time.time() - start_time
    print("Time: ", timePrint)
    serverSocket.sendto(message, address)
serverSocket.close()


#Configure the server so that it randomly drops packets.
# see line 18, 24
#Include information about how long each response took. This will be the RTT.