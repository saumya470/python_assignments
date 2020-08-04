# List comprehensions gives an easy syntax to create one list out of another by applying additional logic to it

# l = [expression for item in iterable if condition]

# To create a list of cube of numbers 1 to 11

'''
lst = [x**3 for x in range(1,11) ]
print(lst)
'''
# Even numbers in list
'''
lst = [x for x in range(2,21,2)]
print(lst)

lst1 = [x for x in range(1,21) if x%2==0]
print(lst1)

'''

# List which contains product of two differenet lists

# Regular logic

# a = [1,2,3,4,5]
# b = [6,7,8,9,10]

# z = []
# for i in range(0,len(a)):
#     z.append(a[i]*b[i])

# print(z)
'''
a = [1,2,3,4,5]
b = [6,7,8,9,10]

z=[a[i]*b[i] for i in range(len(a))]
print(z)
'''
# To create a list with common elements of both lists
'''
a=[2,4,6,8]
b=[1,3,4,7]
res=[]
for i in a:
    if i in b:
        res.append(i)

print(res)
'''

a=[2,4,6,8]
b=[1,2,3,4]
res=[x for x in a if x in b]
print(res)