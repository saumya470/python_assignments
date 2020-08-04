
import socket

s = socket.socket() # Creating an object

s.connect(('localhost',4000))


msg_from_client = input('Enter the msg: ')

s.send(msg_from_client.encode())

msg = s.recv(1024)    # bytes is the buffer size

# Continue listening as long as there is a message
while msg:
    print('Received from server:', msg.decode())        # Since the message is encoded on server side
    msg = s.recv(1024)

s.close()