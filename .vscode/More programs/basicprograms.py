'''
#Read and siplay student details
id = int(input('Enter student id'))
name = input('Enter student marks')
marks = float(input('Enter student marks'))

print('ID:',id, 'Name:',name, 'Marks:',marks)

#Average of three numbers

a,b,c=[int(x) for x in input('Enter 3 interger numbers').split()]
average=(a+b+c)/3
print('Average is:', average)

'''
#Area of the circle/ Math module
import math
r=float(input('Enter the radius'))
area=math.pi*r**2
print('Area is:',area)
