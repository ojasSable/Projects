import string
import random

def randomPwdGen(pwd_len,num_uppercase,num_lowercase,num_digits,num_splchar):

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    splchars = string.punctuation

    password = ''

    for i in range(num_uppercase):
        password = password + random.choice(uppercase)
    
    for i in range(num_lowercase):
        password = password + random.choice(lowercase)

    for i in range(num_digits):
        password = password + random.choice(digits)
    
    for i in range(num_splchar):
        password = password + random.choice(splchars)

    print(password)

    l = list(password)
    password=''.join(random.sample(password,len(password)))
    return password


pwd = randomPwdGen(4,1,1,1,1)
print(pwd)