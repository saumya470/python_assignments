

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
  
#check the above function 

byte_text = b'bHi'
# text = byte_text.decode()
# s = 3
# print("Text  : " + text)
# print("Shift : " + str(s))
encrypt(byte_text.decode(),3)