# This is used to de-serialize or unpickle the contents of the file created 


import pickle

f = open('Student.dat','rb')

obj = pickle.load(f)

obj.display()                   #We can access the methods of the class created in that class through this object

f.close()