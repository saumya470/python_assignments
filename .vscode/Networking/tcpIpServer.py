# Socket programming - to establish communication between server and client using the TCP/IP protocol
# 1. Create server by opening up a socket
# 2. Bind to a machine and port number
# 3. Machine starts listening on the port on that machine and then the client can connect to it
# 4. Once connectionn is established, messages are sent and received
# 5. Connection is closed 


# This program will create a TCP/IP server, listen to the messages sent by client and send back a message in binary

import socket
host = 'localhost'
port = 4000

# Defining IP protocol -Internet Explorer 4 in socket, TCP?IP communication
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Thi sreturns are socket

# Binding the socket
s.bind((host,port))

print('Server listening on port', port)
s.listen(1)     #Number of connections the server will accept


c,addr = s.accept()            #Accept() methods returns the connection and client address when the client sends a message

print('Connection from', str(addr))


c.send(b'Hello, how are you') # send a message to the client the code in binary
#or 

c.send('bye'.encode())

c.close()

