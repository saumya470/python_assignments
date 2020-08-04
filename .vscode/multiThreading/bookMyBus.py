# Adding logic to multithreading


from threading import *

class bookMyBus:

    def __init__(self,availableSeats):
        self.availableSeats = availableSeats
        self.l = Lock()


    def buy(self,seatsRequested):
        self.l.acquire()
        print('\nSeats available are: ',self.availableSeats)
        if (self.availableSeats>= seatsRequested):
            print('\nConfirming a seat\n')
            print('\nProcessing payment\n')
            print('\nPrinting ticket\n')
            self.availableSeats = self.availableSeats - seatsRequested
        else:
            print('Sorry no seats are available')
        self.l.release()


obj = bookMyBus(10)                         #Passing availableSeats
t1 = Thread(target=obj.buy,args=(6,))       #Passing seatsRequested through the thread, args defines the argument in the method buy as an iteratible list
t2 = Thread(target=obj.buy,args=(5,))
t3 = Thread(target=obj.buy,args=(2,))       #args needs to be passed as a list


t1.start()
t2.start()
t3.start()