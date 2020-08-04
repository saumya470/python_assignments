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
        

#Implementing wildcard
mystr='bechurchchbbbchbbbbcnh'
pattern='ch'
print(mystr.count(pattern))

'''
'''
Input and Output functions challenge
This Problem belongs to the Input and Output functions section where you need to have input as a number .This number strictly needs to be an integer as per the constraints given.Your input must not accept strings and floating point numbers and your program should display the digits by mathematical operations and not by iterating the number as a python string. This can be revision of your operands and operators section.
Happy Coding !

Input- Accept an integer as an input where 0<=N<=10000
Output- Print all the digits of the number from left to right, each digit in new line.


lst=[]
l=0

num=int(input('Enter a number between 0<=N<=10000:'))

while l>=0 and num!=0:
        l=num%10
        lst.append(l)
        num=num//10
        
for i in reversed(lst):
    print(i)
    
    
'''
'''
#Operators and Operands challenge problem
num_list=[int(num_list) for num_list in input('Enter the numbers of the list separated by space').split(' ')]

def getOddNum(num_list):
    oddNum=0

    for i in num_list:
        oddNum=oddNum^i
    return oddNum

print(getOddNum(num_list))
'''

'''
def fun(x):
    x[0]=5
    return x
g=[7,8,9]
print(fun(g),g)
'''
'''
# Program that takes user input in Farenheit and converts and displays it in Celsius
c=int(input('Enter the temperature in Celsius - '))
f=(c*9/5)+32
print('Temperature in Farenheit is - ', int(f))
'''
'''
# Creating a right angle traingle based on the input given. Also hashing out numbers that are not even or odd as per the given number.
n=int(input('Enter number between 1 to 10 : '))
print(n)
i=1
j=n-1
while j>=0:
    while i<=n:
        print(j,i)
        j-=1
    i+=1
'''


'''
s=' '
h='#'
n=int(input('Enter number between 1 and 10: '))
i=1
j=n-1
d=str(i)
if (n%2!=0):
    while(i<=n and j>=0):
        if(i%2!=0):print(s*j,d*i)
        else:print(s*j,h*i)
        i=i+1
        j=j-1
        d=str(i)
else:
      while(i<=n and j>=0):
        if(i%2==0):print(s*j,d*i)
        else:print(s*j,h*i)
        i=i+1
        j=j-1
        d=str(i)  


''' 
'''   
print(s*j,d*i)
i=i+1
j=j-1
d=str(i)
print(s*j,d*i)
i=i+1
j=j-1
d=str(i)
print(s*j,d*i)
i=i+1
j=j-1
d=str(i)
print(s*j,d*i)
'''
'''
#Command Line arguments
import sys

#Printing the name of the current script
print(sys.argv[0])

#Printing number of arguments
print(len(sys.argv))

#Printing list of the arguments
for i in sys.argv:print(i)

'''
# To check for special numbers
'''
def IsDigitPrime(x):
    i=2
    if x<=1: 
        return False
    while i<x:
        modulo=x%i
        if (modulo == 0):
            return False
        i=i+1
    return True

def SpecialNum(num):
    dig=[int(x) for x in str(num)]
    for j in dig:
        if IsDigitPrime(j)==False:
            return False
    return True

num=input('Enter the number: ')
result=SpecialNum(num)
print(result)

#def SpecialNum(num):
#     while num > 0 :
#         digit = num%10
#         if (IsDigitPrime(digit) == False):
#             print ('Number is not special')
#             return False
        
#         num = int(num/10)
    
#     print ('Number is special')
#     return True
'''

# Funtion to print reverse of a number

# def ReverseNum(num):
#     rev_num=0
#     while num > 0:
#         remainder=num%10
#         rev_num=rev_num*10+remainder
#         num=num//10
#     print(rev_num)   

    
# num=int(input('Enter the number: '))
# ReverseNum(num)




# Funtion to find the square root of a number. Only print the integer part

# def SqrtFun(num):
#     sqrt=int(num**0.5)
#     print(sqrt)

# num=111
# SqrtFun(num)   


'''

i=1
while i<5:
    if i == 6:
        break
    print(i,end=" ")
    i=i+1
else:
    print('Else is also printed')


'''


#To generate Fibonacci series for the first n numbers (n defined by user)
#Using map, output the square of the fibonacci numbers in a list
'''
n1,n2=0,1
n=int(input('Enter N: '))
count = 0
lst=[]
 
if n < 0:
    print('Enter a positive number')
elif n == 1:
    lst.append(n1)
    print(lst)
else:
    while count<n:
        lst.append(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
    

result=list(map(lambda x:x**2,lst))
print(result)


'''

# Inout a list of positive and negative itegers. Using list comprehensions, create a list which contains the square of negative numbers 
# and positive numbers as is
'''
lst=[int(x) for x in input('Enter the numbers separated by space-').split(' ')]
res=[x**2 if x<0 else x for x in lst]
print(res)
'''

#Input a string and return it without the vowels
'''
sen=str(input('Enter a string: '))
vowels = ('a','e','i','o','u','A','E','I','O','U')

for x in sen:
    if x in vowels:
        sen = sen.replace(x,'')

print(sen)
'''
# Find common numbers from two lists using list comprehensions
'''
l1=[1,2,3,4,5]
l2=[3,4,5,6,7]
result=[int(x) for x in l1 if x in l2]
print(result)
'''

#Compute the performance of list comprehension vs. for loop. So, you’ll be writing twofunctions and use the Python time module 
# to measure their execution time

# import timeit

# code_to_test_list='''
# l1=[1,2,3,4,5]
# l2=[3,4,5,6,7]
# result=[]

# def CommonNums_list(i,j):
#     result=[int(x) for x in l1 if x in l2]
#     return result

# CommonNums_list(l1,l2)
# '''

# code_to_test_function='''

# l1=[1,2,3,4,5]
# l2=[3,4,5,6,7]
# res=[]

# def CommonNums_fun(l1,l2):
#     for i in l1:
#         if i in l2:
#             res.append(i)
#     return res

# CommonNums_fun(l1,l2)
# '''

# ex_time_list=timeit.timeit(code_to_test_list,number=100)/100
# ex_time_function=timeit.timeit(code_to_test_function,number=100)/100
# print(ex_time_list,ex_time_function)


# Make a single list comprehension to return two lists, one for even and another for odd numbers
'''
lst=range(0,20)
even_lst=[]
odd_lst=[]

def lists():
    return [x for x in lst if x%2==0 or odd_lst.append(x)]

even_lst=lists()

print('List-',lst,'Even List-',even_lst,'Odd list-',odd_lst)
'''
'''
# Find even numbers from a list of lists of integers using nested list comprehensions
lst=[[1,2,3],[4,5],[6,7,8],[9],[10]]
res=[y for x in lst for y in x if y%2==0]
print(res)

'''


# Read a file as a list
'''
import re 

try: 
    f = open('C:\\Users\Saumya16\Downloads\doc1.txt','a+')
    f.seek(0)
    s = f.read()
    lst_no_punct = re.sub(r'[^\w\s]','',s)
    print(lst_no_punct.split())
    f.write('\nEditing the file through python scripting, wohoooo!')
except FileNotFoundError:
    print('File not found')
finally:
    print(f.read())
    f.close()
'''

# Write a Python program to print the date of all the Sundays of a specified year.
'''
from datetime import date, timedelta

def getSunday(year):
    dt = date(year,1,1) #First day of the given year
    dt = dt + timedelta(days = 6 - dt.weekday()) #First sunday of the given year
    while dt.year == year:
        print(dt)
        dt = dt + timedelta(days = 7)

year = int(input('Enter the year: '))
getSunday(year)'''


# Input and output funtions
'''
lst=[]
l=0

num=int(input('Enter a number between 0<=N<=10000:'))

while l>=0 and num!=0:
        l=num%10
        lst.append(l)
        num=num//10
        
for i in reversed(lst):
    print(i)

'''

# Q1: Extract email extension from the above string using re.findall
textStr = "From john.doe@ab.etc Thu Jun 15 02:04:09 2010"

import re

result = re.findall(r'@\S*',textStr)
print(result)
