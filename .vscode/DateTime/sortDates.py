from datetime import date
import time

#Also, calculating performance of funtion
start_time = time.perf_counter() # This method returns the current time in seconds

l =[]

d1 = date(2016,7,12)
d2 = date(2016,6,12)
d3 = date(2016,8,12)

l.append(d1)
l.append(d2)
l.append(d3)

l.sort() # compares and sorts the dates


time.sleep(3)           #temporarily halts the execution

#printing the sorted list
for i in l:
    print(i) # By default sorted in ascending order

# Calculating program execution time
end_time = time.perf_counter()

print('Execution time:', end_time-start_time)