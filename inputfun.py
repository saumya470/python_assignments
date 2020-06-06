#s=input()
#print(s)

#Typecast - by default input is string
'''
s=input('Enter the day:')
print(s)

#Input an integer
i=int(input('Enter an integer number'))
print(i)
print(type(i))
'''

#Entering multiple inputs, we are adding them in a list, by default split() uses space
'''
lst=[x for x in input('Enter three numbers separated by space').split()]
print(lst)
'''

#Converting the input to int
lst=[int(x) for x in input('Enter three numbers separated by commas').split(',')]
print(lst)
