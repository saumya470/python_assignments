#Runtime polymorphism is free in python, meaning that it can be done dynamically
#For eg, instead of creating different objects for differnt classes (TreeSeries and FiveSeries), we can create a single object bmw 
# and assign it to the differnt class objects


class BMW:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):                                        #This is a method of th parent class
        print('Starting the car')                           #which will be inherited by the child class

    def stop(self):                                         # ""
        print('Stopping the car')

class ThreeSeries(BMW):                                         #Syntax to define it is a child class of class BMW

    def __init__(self,cruiseControlEnabled,make,model,year):    #It needs to have all the inherited intances of parent class in addition to its own
        BMW.__init__(self,make,model,year)                      #First line of the child class is always parentclass.__init__(instances)
        self.cruiseControlEnabled = cruiseControlEnabled     

    def startThreeSeries(self):
        print('Three series has started')                       #This method is the own one for the child class

    def start(self):                                            #If the same name of a method as the parent is used with different functionality 
        print('Starting the button of three series')             #inside the child class, the functionality is overridden

class FiveSeries(BMW):                                          #Second child class

    def __init__(self,parkingAssisstEnabled,make,model,year):
        super().__init__(make,model,year)                      #Alternatively, can use inbuilt keyword super(). to invoke the constructors of parent class (remove instance self)
        self.parkingAssisstEnabled = parkingAssisstEnabled

    def start(self):                                            #This method is local to FiveSeries() only
        super().start()                                         #Using the in-built keyword super(). to invoke methods of the parent class
        print('Starting the button for five series')


# threeSeries = ThreeSeries(True,'BMW','328i',2018)               #Creating an object of the first child class
# print(threeSeries.cruiseControlEnabled)                         #Printing  the instances
# print(threeSeries.make)
# print(threeSeries.model)
# print(threeSeries.year)
# threeSeries.start()                                             #Invoking method from the parent class
# threeSeries.startThreeSeries()                                  #This method is local to this class

# fiveSeries = FiveSeries(False,'BMW','530e','2019')
# print(fiveSeries.parkingAssisstEnabled)
# print(fiveSeries.make)
# print(fiveSeries.model)
# print(fiveSeries.year)
# fiveSeries.start()                                              #This should invoke start() from parent class and FiveSeries
# fiveSeries.stop()                                               #Invoking method from parent class


bmw = ThreeSeries(True,'BMW','328i',2018)              #Creating an object bmw which will be used dynamically
print(bmw.cruiseControlEnabled)                         #Printing  the instances
print(bmw.make)
print(bmw.model)
print(bmw.year)
bmw.start()                                             #Invoking method from the parent class
bmw.startThreeSeries()                                  #This method is local to this class

bmw = fiveSeries = FiveSeries(False,'BMW','530e','2019') # Object bmw has been reassigned for another class
print(bmw.parkingAssisstEnabled)
print(bmw.make)
print(bmw.model)
print(bmw.year)
bmw.start()                                              #This should invoke start() from parent class and FiveSeries
bmw.stop()                                               #Invoking method from parent class
