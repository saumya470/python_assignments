#Exceptions are run time errors and if not handled correctly can cause one of the three things
#1)Cause the program to terminate unexpectedly (and the code after it will not run), 2) un-friendly msg is displyed to the user, 
# 3)unproper shut down of databases or APIs.

#Exception is used as a class
#Code that might cause an exception is written in the try-except block
#If exception is not raised, code can go to the else block
#Finally block is executed irrespective of whether an exception is raised or not so all clean up code to close APIs can go in this

#Below is the exception hierarchy
#BaseException
#Exception
#This has two classes - > StandardError and Warning
#StandardError - > EOFError, ZeroDivisionError, IndentationError
#Warning - > DeprecatedWarning, ImportWarning

#Below is an example


try:
    f = open('myFile1238','w')
    a,b = [int(x) for x in input('Enter two numbers: ').split(' ')]
    c =a/b
    f.write('Writing %d into file'%c)
except ZeroDivisionError:
    print('Please enter non-zero numbers')
else:
    print('You have entered a non-zero number')
finally:
    f.close()
    print('File closed')
print('Code after exception')