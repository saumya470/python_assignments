# This program will create the file client, send the name of the file it wants the server to read and displaying the contents on the console


import socket

s = socket.socket() # Creating an object

s.connect(('localhost',6767))

# Prompt the user to enter filename

filename = input('Enter a file name: ')

s.send(filename.encode())

content = s.recv(1024)

print(content.decode())


s.close()
