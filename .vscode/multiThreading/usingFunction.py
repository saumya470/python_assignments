# Creating a new thread using funtion

from threading import *

# Create the funtion
def displayNumbers():
    i=0
    print(current_thread().getName())   # Printing thread name
    while i<= 10:
        print(i)
        i=i+1


print(current_thread().getName())
t = Thread(target = displayNumbers)        # Thread is created by creating an object of Thread class, target = function to be used

# To start the thread
t.start()
