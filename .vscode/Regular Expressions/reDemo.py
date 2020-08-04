# Sequence characters - to match a single character in a string
# \d - any digit (0-9), \D - any non-digit character, \s - white space, \S - non-white space, \w - alpha-numeric value, 
# \W - non-alpha numeric  character, \b - space around words, \A - to search atthe start of a string, \Z - matches at the end of the string

import re   #regularexpression

# search() method

str = 'Take up one idea. One idea at a time'
#Find all substrings which start with 'o' and have two charaters folloing it
result = re.search(r'o\w\w',str) # This will return the first substring with the citeria
print(result.group()) #This method give the exact stirng which matches


# findall() and match()

str = 'Take up one idea. one idea at a time'
result = re.findall(r'o\w\w',str)           #rerurns a list, empty list if nothing is found
print(result) 

result = re.match(r'o\w\w',str)         #This only searches at the beginning of the string     
print(result) 

result = re.match(r'T\w\w',str)            
print(result) 
print(result.group())       #cannot invoke group() method is 'None' is returned


# split() - splits the given string into a list of substrings depending on the delimiter passed

str = 'Take 1 up one 23 idea. one 42-3-2020 5 idea 1-2-2011 at a time'

result = re.split(r'\d+',str)            #Split by one or more digits
print(result)

# sub() - replace all or substitute the given string with a new string

result = re.sub(r'one','two',str)            
print(result)

# Quantifiers = used to match multiple characters
# + repetition, example - \d+ - one or more digits, 
# * -  0 or more precedings, ? - 0 or one, {m} - exactly m occurance, {m,n} - min to max number of occurances

print(str)
result = re.findall(r'i\w+',str)          
print(result) 

result = re.findall(r'o\w*',str)          
print(result) 

result = re.findall(r'o\w?',str)          
print(result) 

result = re.findall(r'o\w{2}',str)          
print(result) 

# Matching dates

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)          
print(result) 

# Special characters 
# / - escape character
# . = any character except new line
# ^ - to search at the beginning
# $ - search at the end of the string
# [..] - range of characters
# [^...] - matches all characters except in this range
# (...) - any regular expression
# (R|S) - multiple regular expressions, R or S



result = re.search(r'^T\w*',str)
print(result.group())