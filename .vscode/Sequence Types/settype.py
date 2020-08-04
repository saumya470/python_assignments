#Does not allow duplicates; defined by curly  braces

s={10,20,30,'xyz',10,5}
print(s)
print(type(s))

# To update set
s.update([77,4])
print(s)

#Since sets do not guarantee any order, we cannot slice, index or repeatition
#print(s[0])
#print(s*3)

#To Remove
s.remove(10)
print(s)

#Frozen set - does not allow to perform update/remove operations
f=frozenset(s)
print(f)
#f.remove(4) #gives and error
