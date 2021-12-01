import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*"
length = input('password lenght?=') 
length  = int(length)
Number = input('how many passwords =' )
Number = int(Number)
for c in range(Number): 
    password = ''
    for i in range(length):
        password +=  random.choice(chars)  
    print(password)