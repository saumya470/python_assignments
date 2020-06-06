'''Tuple is a list which cannot be modified
i.e., we cannot use methods like append(), extend(), insert(), remove(), clear()
'''
tpl=()
print(tpl)

tpl=(40,50,40,'XYZ')
print(tpl)
print(type(tpl)) # This considers is class Tuple

#Difference of a comma -
#For a single element in a list or tuple, ALWAYS use a comma at the end
tpl=(40)
print(type(tpl)) # Considers int

tpl=(40,) # Considers a tuple
print(type(tpl))
#Indexing
tpl=(2,5,8,1,-10,'abc')
print(tpl[4])
#Repeatition
print(tpl*3)
#Counting the elements
print(tpl.count(5))
print(tpl.index('abc'))

lst=[67,34,34,'xyz']
print(lst)
print(type(lst))
#Converting a list to Tuple
tpl1 = tuple(lst)
print(tpl1)
print(type(tpl1))
