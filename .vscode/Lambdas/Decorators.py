#Decorator is a function that takes a funtion as input and returns another function after performing some additional processing 
# to the funtion taken as input i.e. decorates it 
# Inside the funtion that is returned from the decorator, there is logic that will invoke the input funtion, 
# takes the result of it and performs additional logic on it

# Create a decoartor funtion that will return the double the number returned by another funtion
'''
Steps to create a Decor function
1. Create a function decor() which takes another funtion fun() as a parameter
2. Define another funtion, inner() which will invoke the input funtion fun(), perform and return the logic to double it 
3. Close the decor funtion by returning the inner funtion()
4. Define the funtion that will be decorated
5. Invoke the decore function

'''
'''
def decor(fun):
    def inner():
        result = fun()                  #Invoking the fun() function
        return result*2                 #Performing the logic on fun()
    return inner                        #Close the decor funtion by returning the inner funtion

def num():
    return 5

resultfun = decor(num)                  #We are passing the num funtion (which will be decorated) as a paramaetre to the decorator
print(resultfun())                      #to get the final result in resultfun
'''

# In order to directly apply a funtion to decorator use @decor on top of the respective funtion
# This way we can directly print the reult by invoking the funtion to be decorated

'''
def decor(fun):
    def inner():
        result = fun()                  #Invoking the fun() function
        return result*2                 #Performing the logic on fun()
    return inner                        #Close the decor funtion by returning the inner funtion

@decor                                  #Used to indicate that this funtion will ALWAYS be used to the decorator
def num():
    return 5

print(num())                            #Directly invoke num()

'''





# String decorators
# Create a funtion hello() that will take the name and return 'Hello' + name
# Create a decorator that will decoarte the Hello funtion and return hello() + 'How are you'

def decor(fun):
    def inner(n):
        result = fun(n)
        result = result + ' How are you?'
        return result
    return inner

@decor
def hello(name):
    return 'Hello ' +name

name=input('Enter your name: ')
print(hello(name))

