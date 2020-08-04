#Using a class that does not inherit the Thread class

from threading import *
from time import sleep

class  myThread:

    def displayNumbers(self):
        i=0
        print(current_thread().getName()) 
        sleep(2)  
        while i<= 5:
            print(i)
            i=i+1


obj = myThread()    #Creating an instance of the class
t1 = Thread(target=obj.displayNumbers)           #Spawning the new thread to the thread object
t1.start()                                       #by passing the instance.method name as the target parameter


# To use multi-threaing, use as below
t2 = Thread(target=obj.displayNumbers)
t2.start()

# Svheduling of the trhreads is upto th einterpreter
'''
t3 = Thread(target=obj.displayNumbers)
t3.start()

t4 = Thread(target=obj.displayNumbers)
t4.start()
'''
'''t4 = Thread(target=obj.displayNumbers)
t1.start()'''