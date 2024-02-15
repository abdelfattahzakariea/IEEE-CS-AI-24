import random
import string

char = string.ascii_uppercase + string.ascii_lowercase + string.digits 
passward=''             #.join(random.choice(char) for x in range(8))        
for x in range(8):
    passward += random.choice(char) 
print(passward)
