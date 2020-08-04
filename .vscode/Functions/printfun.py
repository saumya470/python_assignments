print()
print('Hello*3')
print('All the power \nis within you')
a,b=10,20
print(a,b)
print(a,b,sep=',')
print(a,b,sep='+++++++\n++++++')

student_name='John'
marks=89.9546
print('Name is:',student_name,'\nMarks are:',marks)
#Similarly keep a placeholder such as %i for integer,%f for float,%s for string
print('Name is: %s\nMarks are: %f'%(student_name,marks))
print('Name is: %s\nMarks are: %.2f'%(student_name,marks)) #Formatting the decimal point numbers
#Using string as a method, curly braces are used as placeholders
print('Name is: {}\nMarks are:{}'.format(student_name,marks))
#Using index in above statement
print('Name is: {0}\nMarks are: {1}'.format(student_name,marks))