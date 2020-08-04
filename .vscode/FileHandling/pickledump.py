#This is used to serialize or dump an object into another file
# Here we are dumping an object of class Student (in Student.py) into a .data file named Student, this will create this new file
# This is a binary file and we unpickle to get access to it

import pickle,student                           #importing pickle module and also the class whose object we need to dump

f = open('Student.dat','wb')                    # Creating an object to open the file
s = student.Student(123,'Henry',90)             #Creating an instance student from Student module and passing the parameters
pickle.dump(s, f)                               #object is the object of the file we want to dump, file is the file where

f.close()



 