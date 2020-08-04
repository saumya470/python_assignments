'''# Bytes and bytearray
#Create a fromlist
lst=[10,20,30,40]
print(type(lst))

#Convert to byte which can have values in the range 0<=x<256
b=bytes(lst)
print(type(b))
print(b)
#b[3]=33 # This gives an error

b1=bytearray(lst)
print(type(b1))
print(b1)
b1[3]=33
print(b1)
# Indexing can be  done on bytearrays but not bytes. No slicing or repeatition can
# be done on either
'''

str_text = 'Hello'
print(str_text)
byte_text = str_text.encode()
print(byte_text)
new_str_text = byte_text.decode('utf-8')
print(new_str_text)
'''
lst = ['h','i']
print(lst)
byte_text = bytes(lst)
print(byte_text)
#print(byte_text.decode('utf-8'))'''