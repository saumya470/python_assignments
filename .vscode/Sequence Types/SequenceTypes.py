'''Sequence of values such as a List, Sets and Dictionary
'''
# String operations

s='You are awesome'
print(s)
#Multiple lines
s1='''You are
the
creator of
your destiny'''
print(s1)

#Indexing
print(s[0])
print(s[2])

#Printing multiple times/ repeatition
print(s1*2)

#length of a variable
print(len(s1))

#Slicing a string - It DOES NOT include the character at the ending index
print(s[0:5])
print(s[0:]) #No ending index defined - This goes till the end from 0 index
print(s[:9]) #No starting index defined - It goes from 0 to 8
print(s[8:])
print(s[-3:-1]) #-1 means the last character of the string, so this will start printing from o and print m but does not include e
# Step value
print(s[0:10:2]) # 2 is the defined step number, i.e., it will print the alternate characters
print(s[::-1]) # Printing in reverse order, no start or end defined but will decreament


#Strip spaces
t='    You             are awesome    '
print(len(t))
print(t.strip()) # strips at beginning and ending
print(t.lstrip()) # Strips left spaces
print(len(t.rstrip())) # Strips right spaces

u='Hello'
print(u[::-1]) # printing in reverse

# Find a substring
print(s.find('awe'))
print(s.find('aw',0,len(s))) # Defining the start and ending points
print(s.find('aw',0,7))# returns -1 if it cannot find
# Find occurrence of substring
print(s.count('a'))
#Replacing text
print(s.replace('awesome','super'))

# Find UPPER, lower and Title case
print(s.upper())
print(s.lower())
print(s.title())


o=10
p=20.54
q=True
r='I am the best'
print(o,p,q,r)
