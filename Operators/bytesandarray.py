# Bytes and bytearray
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
