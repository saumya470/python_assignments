class Car:
    def __init__(self,make,year):
        self.make = make
        self.year = year

    class Engine:                           #Inner class
        def __init__(self,uid):
            self.uid = uid
            
        def start(self):                    #Method for the inner class
            print('Engine started')
                

c = Car('BMW', '2017')                            #Creating an object of outer class
e = c.Engine(123)                                 #Creating an object of inner class by invoking the outer class
e.start()