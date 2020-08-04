# This program will create a TCP/IP client which will connect to the server on port 4000 and receive messages from the server and displays
# it on the console

import socket

s = socket.socket() # Creating an object

s.connect(('localhost',4000))

msg = s.recv(1024)    # bytes is the buffer size

# Continue listening as long as there is a message
while msg:
    print('Received from server:', msg.decode())        # Since the message is encoded on server side
    msg = s.recv(1024)

s.close()
