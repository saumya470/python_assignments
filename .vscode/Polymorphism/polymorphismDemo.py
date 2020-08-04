# Poly means multi and morphism means behavior i.e. different types of behavior based on data or objects that the functions are dealing with.
# # Different ways to implement
# 1. Duct typing
# 2. Duct typing to do depency injection
# 3. + operator for overloading to perform multiple operations.
# Method overriding - run time polymorphism


# #Duck typing - It is the dynamic nature of the object passed in a method or funtion
# For eg, if two different classes - Duck and Human have a method - talk(), then an object from another method can be dynamically used to call 
# the talk() method from any class. Depending on what object is being passed, the function can do different/multiple things

class Duck:
    def talk(self):
        print('Quack Quack')

class Human:
    def talk(self):
        print('Hello')

def callTalk(obj):
    obj.talk()

d = Duck()                      #Behaves as a method of class Duck when object of class Duck is passed
callTalk(d)

h = Human()                     #Behaves as a method of class Humanh when object of class Human is passed
callTalk(h)

