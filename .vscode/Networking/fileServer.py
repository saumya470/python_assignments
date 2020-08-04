
# Creating a server that receives a file sent from the client, sends back the content of the file the client has requested for

import socket
host = 'localhost'
port = 6767

# Defining IP protocol -Internet Explorer 4 in socket, TCP/IP communication
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Thi sreturns are socket

# Binding the socket
s.bind((host,port))

print('Server listening on port', port)
s.listen(1)     #Number of connections the server will accept


c,addr = s.accept()            #Accept() methods returns the connection and client address


# Reading the data that comes in
filename = c.recv(1024)

try:
    f = open(filename,'rb')
    content = f.read()
    c.send(content)
    f.close()
except FileNotFoundError:
    c.send('bFile does not exist') # Sendig the file/ message back to client


c.close()

