# Classes as a blueprint for objects and help to feine our own datatype
# Components of a class: variables, methods
# Creating tihe first class
# Method is a function associated with a class


class Product:                              #name of the class is Product

    def __init__(self):                     #init (or initialize) method helps to define and assign the variables at the same time/Constructor
        self.name = 'Iphone'                    
        self.description = 'Its awesome'
        self.price = 700

    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)

p1 = Product()                              #Create an object or instance of class Product

p1.display()

#Alternatively, withot using display method

p2 = Product()                              #Creating another object

print(p2.name)                              
print(p2.description)
print(p2.price)





                    

