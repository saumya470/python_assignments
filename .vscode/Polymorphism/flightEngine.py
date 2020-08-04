#Dependency Injection - injecting an object into another object as required
# Eg, we have a Flight that needs an Engine to fly it. We can inject different types on engines - BoingEngine or AirbusEngine 
# into Flight object dynamically
# We need not inherit any classes because Python allows the object engine to dynamically use the start method of any class

class Flight:
    def __init__(self,engine):    #Definining a constructor to create a dynamic instance variable engine which can perform Dependency injection
        self.engine = engine

    def startEngine(self):            #Defining a method
        self.engine.start()           #We are assuming that this method will have a start method which will be invoked by engine object

class AirbusEngine:
    def start(self):
        print('Starting Airbus Engine')

class BoingEngine:
    def start(self):
        print('Starting Boing Engine')


#Creating objects
ae = AirbusEngine()
f1 = Flight(ae)
f1.startEngine()

be = BoingEngine()
f2 = Flight(be)
f2.startEngine()


