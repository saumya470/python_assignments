#Write an assertion statement for even numbers
'''
num = int(input('Enter a number- '))
assert num%2==0, 'You have entered an odd number' #This message is displayed when the condition is not met
'''
# The code after assert statement is not displayed and so we can use a try catch block
# Also, printing the assertion error makes it user-friendly


try:
    num = int(input('Enter a number- '))
    assert num%2==0, 'You have entered an odd number' 
except AssertionError as obj:
    print(obj)

print('After the assertion')


