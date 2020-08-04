import logging

logging.basicConfig(filename='myFile.log',level=logging.DEBUG)

try:
    f = open('myFile','w')
    a,b = [int(x) for x in input('Enter two numbers: ').split(' ')]
    c =a/b
    f.write('Writing %d into file'%c)
    logging.info('Division in progress')
except ZeroDivisionError:
    print('Please enter non-zero numbers')
    logging.error('Division by zero')
else:
    print('You have entered a non-zero number')
finally:
    f.close()
    print('File closed')
print('Code after exception')