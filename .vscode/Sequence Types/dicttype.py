'''dict1={1:'John',2:'Bob',3:'Bill'}
print(dict1)
print(type(dict1))
print(dict1.items())
print(dict1.keys())
print(dict1.values())


k=dict1.keys()
for i in k:
    print(i)

v=dict1.values()
for i in v:
    print(i)

#Print the values via key
print(dict1[2])

#Delete via keys
del dict1[2]
print(dict1)
'''

#Assignment
lst = ['India','Nepal','Bhutan']
print(lst)
#Adding a country in the end
lst.append('Sri Lanka')
print(lst)
#Removing a country by index
del(lst[0])
print(lst)
#Adding a country in the middle
lst.insert(1,'China')
print(lst)

#Similarly for sets
s1={'India','Australia','Spain'}
print(s1)

#Adding a coutry in the set
s1.update(['Sri Lanka'])
print(s1)
#removing a country from the set
s1.remove('India')
print(s1)
#Adding a country
s1.update(['Italy'])
print(s1)
