#password generator
import random 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "{}@#$%^&*()"
all = upper+lower+numbers+symbols
length = 14
password ="".join(random.sample(all,length))
for i in range(10):
    password ="".join(random.sample(all,length))
    print(password)
