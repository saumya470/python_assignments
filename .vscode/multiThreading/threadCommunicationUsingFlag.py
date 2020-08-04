# In multithreading, threads have to often communicate with each other to get the job done. A common pattern is the Producer thread 
# and Consumer thread. The Producer thread is responsible for creating some work, for example, recieving all orders from the user. It prepares
# a list of all orders. Consumer thread is responsible for processing the orders and shipping them.
# Now Consumer thread needs to know when the processing is done and it can start its work. One way is to use a flag - ordersPlaced
# on Producer thread. The Consumer thread continuously keeps monitoring till it is True. Only when a list is prepared, the flag is flipped to 
# True


from threading import *
from time import *

class Producer:

    def __init__(self):
        self.products = []                  #Initially an empty list
        self.ordersPlaced = False           #This is the boolean flag 


    def produce(self):
        for i in range(1,5):
            self.products.append('Product'+str(i))
            print('Product added')
            sleep(1)
        self.ordersPlaced = True        # Once we have a list of 5 items, this flag becomes true

class Consumer:

    def __init__(self, prod):           #This needs an instanceof Producer thread
        self.prod = prod

    def consume(self):
        while self.prod.ordersPlaced == False: # It will keep checking as long as the flag is False
            sleep(1)

        print('Orders shipped ',self.prod.products) # It will ship it when done


p = Producer()
c = Consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()



        

    


