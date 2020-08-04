

import socket


# Defining IP protocol -Internet Explorer 4 in socket, TCP?IP communication
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Thi sreturns are socket

# Binding the socket
s.bind(('localhost',4000))

print('Server listening on port', 4000)
s.listen(1)     #Number of connections the server will accept


c,addr = s.accept() 

# Reading the data that comes in
msg_from_client = c.recv(1024)


'''while msg_from_client:
    msg_from_client = c.recv(1024)'''

c.send(msg_from_client)

c.send(encrypt(msg_from_client.decode(),3))

c.send(b'Message from server') # send a message to the client the code in binary

c.send('\nbye'.encode())


c.close()


#A python program to illustrate Caesar Cipher Technique 
def encrypt(text,s): 

    
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 

        elif(str(char) == ' '):
            result += ' '
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return print(result.encode())
  

