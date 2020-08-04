
from threading import *
from time import *

class Producer:

    def __init__(self):
        self.products = []                  #Initially an empty list
        self.c = Condition()                #Creating a condition object


    def produce(self):
        self.c.acquire()                    #Acquiring a lock on condition object so that we are in a synchronized context

        for i in range(1,5):
            self.products.append('Product'+str(i))
            sleep(1)
            print('Product added')
        self.c.notify()                     #Once producer has done the job we notify and release the lock
        self.c.release()

class Consumer:

    def __init__(self, prod):           #This needs an instanceof Producer thread
        self.prod = prod

    def consume(self):                  #This will be executed in parallel
        self.prod.c.acquire()       
        self.prod.c.wait(timeout=0)
        self.prod.c.release()
        print('Orders shipped ',self.prod.products) # It will ship it when done


p = Producer()
c = Consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()



        

    


