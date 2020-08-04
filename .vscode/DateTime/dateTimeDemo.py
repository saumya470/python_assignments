import time, datetime

epochseconds = time.time() #This method gives the time since beginning
print(epochseconds)

t = time.ctime(epochseconds) # To convert this to current time
print(t)

dt = datetime.datetime.today() #datetime class from datetime module contains today() method
print(dt)
print(dt.day,dt.month,dt.year)
print(dt.hour,dt.minute,dt.second)

#Formatting
print('Current date : {}/{}/{}'.format(dt.month,dt.day,dt.year)) # Format method allows to automatically format the date, {} act as placeholders
print('Current time : {}:{}:{}'.format(dt.hour,dt.minute,dt.second))