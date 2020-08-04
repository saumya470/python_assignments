import sys #this is the module which contains the list to contain the comand line arguments in python
lst=sys.argv
for i in lst:print(i) # This will print all the elements in the list which is currently the name of the script or program by default
'''

print(len(lst)) # Contains only one element so far

print(lst[0]) # To access elements of the list
'''
#print(lst[0])

print('Product is: ', int(lst[1])*int(lst[2]))

