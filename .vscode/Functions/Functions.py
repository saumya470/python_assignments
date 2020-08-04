
#Funtion to find out the avergae of two numbers
'''
#Defining the function
def avg(a,b):
    print('Average of two numbers is:', (a+b)/2)

#Invoking the function
avg(10,20) 
'''

#Alternatively we can return the result instead of printing
'''
def avg(a,b):
    return (a+b)/2

result=avg(10,20)

print('The average is:',result)
print('The average is:', avg(10,40))

'''

# Creating a calculator to return multiple functions - addition, subtraction, division

'''
def calc(a,b):
    x=a+b
    y=a-b
    z=a*b
    u=a/b
    return x,y,z,u

result=calc(30,15) # Result contains the output of the function in the form of a tuple

for i in result: print(i)


'''

#Global and local variable

'''
x=123

def Display():
    x=678
    print(x)
    print(globals()['x'])

print(x)
Display()
z=Display
z()
z()
z()
'''

#Function inside a funtion
'''
def display(name):
    def message():
        return 'Welcome '
    result=message()+name
    return result

print (display('Saumya'))
'''

#Function as a parameter to another function
'''
def display(fun):
    return 'Hello '+fun

def name():
    return 'Saumya'

print(display(name()))

'''

#Return a function within another function
'''
def display():
    def message():
        return 'Hello'
    return message

fun=display()
print(fun())
'''

#List in a funtion


def fun(lst):
    for i in lst: print(i)

fun([1,2,3,4])

'''
#Keyword arguments

def avg(a,b):
    print(a)
    print(b)
    return((a+b)/2)

print(avg(a=10,b=20))
'''