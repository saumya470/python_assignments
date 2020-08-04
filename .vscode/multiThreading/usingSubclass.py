# Thread extending the Thread class
# Here we are creating a new class which extends the class Thread and overidding the method run()
from threading import Thread

class myThread(Thread):
    # Overriding run method
    def run(self):
        i=0
        while i<= 10:
            print(i)
            i=i+1


t = myThread() # Creating an object of class
t.start() # To invoke the created thread