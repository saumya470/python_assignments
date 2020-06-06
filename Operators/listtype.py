#Empty list
l1=[]
print(l1)

#Adding different kind of elements
l2=[10,20.5,'Saumya',-5,False]
print(l2)
#Indexing
print(l2[2])
#Slicing
print(l2[3:5])
#Repeatition
print(l2*4)
#Length of list
print(len(l2))

# 3 methods to dynamically add or remove elements from a list
l2.append(49)
print(l2)
#Delete by value
l2.remove('Saumya')
print(l2)
# Delete by index
del(l2[1])
print(l2)

# Remove allelements fromlist
l2.clear()
print(l2)
#Min max
l3=[10,20.5,49,-15]
print(l3)
print(max(l3))
print(min(l3))

l3.insert(2,99) #Insert(index,value)
print(l3)

l3.sort()#Sorting
print(l3)
l3.sort(reverse=True)#Sort in descending order
print(l3)
