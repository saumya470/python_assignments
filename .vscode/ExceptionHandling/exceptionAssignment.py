# Ask the user to enter a password. Create a custom exception - InvalidPasswordException which is invoked if the password is less than 8 
# characters, raise and and handle it

class InvalidPasswordException(Exception):
    pass

try:
    f = open('PswdFile','w')
    pswd = str(input('Enter the password- '))
    if len(pswd) < 8:
        raise InvalidPasswordException
    else:
        f.write(pswd)

except InvalidPasswordException as pwd:
    print('Password is too short, please re-enter')

finally:
    print('After exception')
    f.close()




