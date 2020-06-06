''' Week 2 challenges
Standard/ built-in datatypes

i.  Numeric - integer, float(dp) and complex no
ii. Boolean - true or false
iii. Sequence -string (characters), list (data items) and tuple (data items in parentheses)

Type () function

To be attempted:
A.  Write a Python program which accepts the radius of a circle from the user and compute the area of the circle.
B.  Write a Python program which accepts a sequence of comma-separated numbers from the user and generates a list and a tuple with those numbers. Sample data: 3, 5, 7, 23
Output:
List: ['3', ' 5', ' 7', ' 23']
Tuple: ('3', ' 5', ' 7', ' 23')

C. 	Write a Python program to test whether a number is within 100 or 1000 or 2000
D.	Write a Python program to check whether a specified value is contained in a group of values. Test Data:
3 -> [1, 5, 8, 3]: True
-1 -> [1, 5, 8, 3]: False
'''
#A
'''
print('Enter radius:')
r=input()
radius = float(r)
area=3.14*radius*radius
print('Area of the circle is:', area)

#B

print('Enter a sequence of comma separated values ')
lst=input()
lst=lst.split(',')
print('Your list is:',lst)
tpl=tuple(lst)
print('Your tuple is:',tpl)


#C
print('Enter a number')
num=float(input())
if num<=100:
    print('Number is less than or equal to 100')
elif num>100 and num<=1000:
    print('Num is greater than 100 and less than or equal to 1000')
elif num>1000 and num<=2000:
    print('Num is greater than 1000 and less than or equal to 2000')
else:
    print('Num is greater than 2000')

#D

lst=[1,5,8,3]
print('Enter a number:')
num=int(input())
if num in lst:
    print('True')
else:
    print('False')


# Assignment on Operators and operands - Week 3
print('Enter the marks of 5 subjects separated by space')
lst=[int(marks) for marks in input().split(' ')]
per=int(sum(lst)/len(lst))
#print('The average is:',per)
if (per>=90):
    print('Grade is: A')
elif(per>=80 and per<90):
    print('Grade is: B')
elif (per>=70 and per<80):
    print('Grade is: C')
elif(per>=60 and per<70 ):
    print('Grade is: D')
else:
    print('Grade is: F')

#Assignment on Input and Output - Week 3

name = input('Enter your name:')
marks = [int(marks) for marks in input('Enter your marks for 3 subjects separated by space:').split(' ')]
print(name, ', your marks are', marks)
'''
'''
#Assignment Sequence Type week 3
import re 
import fnmatch
str_list = [str(str_list) for str_list in input('Enter your list of words separated by spaces and a character ch').split(' ')]
print('Your list is:', str_list)

filtered = fnmatch.filter(str_list,'ch*')
print(filtered.count('ch'))
'''
from collections import Counter
lst1 = input('Enter string elements separated by space:').split(' ')
ch=input('Enter the character to find:')
print('List 1:', lst1)
#lst1 = ['church','church','chair','choir','kite','kitten']
distint_list=list(Counter(lst1).keys())
lst2=[]
print('List 2:', lst2)
print('DList 1:', distint_list)
#Take it
print('List1 is',lst1)
print('List2 is',lst2)
#for i in range(len(lst)):
for i in range(len(distint_list)):
    elmnt=distint_list[i]
    #print(elmnt.count(ch))
    if elmnt.count(ch)>0:
        print(elmnt, ': This element is in the list')
        for j in range(elmnt.count(ch)):
            lst2.insert(i,elmnt)
    else:
        print(elmnt, ': This element is not in the list')
print(lst2)
        
'''
#Implementing wildcard
mystr='bechurchchbbbchbbbbcnh'
pattern='ch'
print(mystr.count(pattern))

'''




