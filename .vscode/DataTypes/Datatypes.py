'''In Python, we do not need to explicity define a datatype. The variables automatically assign itself
In Python datatypes are categorized into 5 types-
1. None type (NaN) which means no value
2. Integer - int, float, complex, binary, hexa, octa
3. Sequences - str, bytes, bytearray, list, tuple, range
4. Sets
5. Mappings
type is used to understand what datatype is tored in a variable
'''

# Integer dataType
a=100
b=-72
c=0
print(a,b,c)
print(type(a),type(b),type(c))

# Float
x = 1.2
y=0.0
print(x,y)
print(type(x),type(y))

#Complex dataType
d=5+7j
print(d)
print(type(d))

#Binary type, starts with 0B
e=0B1011
print(e)
print(type(e))

#Hexadecimal number starts with 0X (0 1 2 3 4 5 6 7 8 9 A B C D E F)
f=0X7F
print(f)
print(type(f))

#Octadecimal number starts with 0O (digits 0 to 7)
g=0O17
print(g)
print(type(g))

#Bool
h=True
print(type(h))
print(9<8) #returns False

#Convert datatypes by int function
i=int(x)
print(type(i))

#Convert string to Float using float function, binary, Hexadecimal and Octal
j=float("22.5")
print(j)
print(type(j))

k=bin(10)
print(k)

print(hex(10))

print(oct(10))
