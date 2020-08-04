# Abstraction means to hide the complexity and only show the essential features. 
# In Python, abstract classes are classes which provide incomplete functionality, i.e., do not have the implementation in the class itself but
# have atleast one abstract method in it.
#It is left to the sub-class to provide implementation through the abstract method  
# An abstract method is denoted with the @abstractmethod decorator and any child class that inherits an abstract class has to implement it.
# If not implemented, then that child class also becoms an abstract class
# Method signature i.e., number of parameters for the abstarct method should be same in the child class as in the parent class
# Abstraction is done from ABC module
# Two steps for abstraction - 1. Import the module abc to get the decoartor @abstractmethod, 
# 2. Parent class must inherit ABC class from the module (To mandate that the child classes implement abstraction)
# An abastract class cannot be instantiated 

# A class in which all the methods are abstract methods, it is called an Interface.

# Create a class BMW which has two child classes - ThreeSeries and FiveSeries. 
# BMW wants to mandate that all classes should have a method drive()
#We will create a method in parent class

from abc import abstractmethod, ABC
class BMW(ABC):                                         #Inheriting ABC class for abstarction

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):                                        #This is a method of th parent class
        print('Starting the car')                           #which will be inherited by the child class

    def stop(self):                                         # ""
        print('Stopping the car')

    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(BMW):                                         #Syntax to define it is a child class of class BMW

    def __init__(self,cruiseControlEnabled,make,model,year):    #It needs to have all the inherited intances of parent class in addition to its own
        BMW.__init__(self,make,model,year)                      #First line of the child class is always parentclass.__init__(instances)
        self.cruiseControlEnabled = cruiseControlEnabled     

    def startThreeSeries(self):
        print('Three series has started')                       #This method is the own one for the child class

    def start(self):                                            #If the same name of a method as the parent is used with different functionality 
        print('Starting the button of three series')             #inside the child class, the functionality is overridden

    def drive(self):
        print('ThreeSeries is being driven')

class FiveSeries(BMW):                                          #Second child class

    def __init__(self,parkingAssisstEnabled,make,model,year):
        super().__init__(make,model,year)                      #Alternatively, can use inbuilt keyword super(). to invoke the constructors of parent class (remove instance self)
        self.parkingAssisstEnabled = parkingAssisstEnabled

    def start(self):                                            #This method is local to FiveSeries() only
        super().start()                                         #Using the in-built keyword super(). to invoke methods of the parent class
        print('Starting the button for five series')

    def drive(self):
        print('FiveSeries is being driven')


threeSeries = ThreeSeries(True,'BMW','328i',2018)               #Creating an object of the first child class
print(threeSeries.cruiseControlEnabled)                         #Printing  the instances
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start()                                             #Invoking method from the parent class
threeSeries.startThreeSeries()                                  #This method is local to this class

fiveSeries = FiveSeries(False,'BMW','530e','2019')
print(fiveSeries.parkingAssisstEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)
fiveSeries.start()                                              #This should invoke start() from parent class and FiveSeries
fiveSeries.stop()                                               #Invoking method from parent class

# this will give an error since we cannot instantiate and abstract class itself
#b = BMW('BMW','530e','2019')
threeSeries.drive()
