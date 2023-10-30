import random
import string

def password_generator(upercase,special,numbers,lenght):
    '''
    input: uppercase 0 (False) or 1 (True)
           special 0 (False) or 1 (True)
           numers 0 (False) or 1 (True)
           lenght a int > 0
    
    output: str 
    '''

    chars = string.ascii_lowercase
    password = ""

    if upercase == 1:
        chars += string.ascii_uppercase
    if special == 1:
        chars += string.punctuation
    if numbers == 1:
        chars += string.digits
    
    for i in range(lenght):
        password +=(random.choice(chars))

    return password