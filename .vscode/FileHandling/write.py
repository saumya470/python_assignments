# Files are where we organize or store data. There are two types - text and binary(videos, audio etc.)
# f = open('fileName','mode','buffer'), f is the file object
#fileName is the name or path of the file
#mode is for following type - w(write - overrites on existing contect), r(read), a(append - adds new content to the end), w+(write and read)
#r+(read, write, append), a+(append and read), x(exclusive creation - to create a new file)
#For binary file, -> wb, rb etc.
#Buffer, an optional paramenter is space that we can add to add internal buffer, by default it is 4096 or 8092
# f.close() is used to close the file object

#This opens the file for writing

'''
f = open('Myfile.txt','w') 
s = input('Enter text: ')
f.write(s)
f.close()
'''

# To enter multiple lines of data
'''
f = open('Myfile.txt','w') 
print('Enter text (Enter # when done)')
s = ''
while s!='#':
    s = input()
    f.write(s)

f.close()'''

#These modules are used to check if a file exists before writing 
# (os has a submodule 'path' which has a method 'isFile', this returns a boolean, sys module is used to exit if file not exists)

import os, sys                              
if os.path.isfile('MyFile1.txt'):
    f = open('Myfile.txt','w') 
    print('Enter text (Enter # when done)')
    s = input()
    while s!='#':
        f.write(s)
        s = input()
    f.close()
else:
    print('File does not exist')
    #sys.exit()





