################## variables 
'''
# variables => int + float + bolean + string => series of char .

age = 21
print("your age",age,"years old") # not contactnation but link with other and take space by default   
print("your age " + str(age) + " years old") # concatnation not process about int + concat must str + str
print(f"your age { age } years old")# Fstriig
 
x, y, z=1, 2, 3 

a=b=c =1

print(x)

#if you want to take a two num after comma use round func => age = round(age)
age = 2.126021
age = round(age,2)
print(age)

'''
############# Type casting
'''# tow type of casting    explicity + implicity 
##explicity 
age = 21
print (type(age))
age =float(age)
print (type(age))
print(age)

############implicity 

x=20
y=2.0
x/=y
print(x)

'''

############## input
'''
name = input("enter your name : ")   # variables about input typicly stored a string var 
age = input("enter your age : ")   
age = int(age)

print(f"your name : {name}")
print(f"your age : {age} years old")

length = float(input("enter length : "))
print(type (length))

'''
############# built in fun math

'''
import math
x=3.1452
y=5

#result = round(x,2)
#result = abs(x)
#result = min(x,y)
#result = max(x,y)
#$result = pow(x,y)
result =math.sqrt(x) #must import math library 
print(result)

'''

####### if statement and logical operator and, or, (not => for boolean
'''
age = int(input("enter your age : "))

if age > 18:
    print("university student")
elif age > 15 and age<18:
    print("sacendory student")
    print("--------  -------------")
else:
    print("primary student")
    
'''
############### string 
'''
name = input("enter your name : ")

#result = len(name)
#result = name.find("o")
#result = name.rfind("o")
#result = name.capitalize()
#result = name.upper()
#result = name.lower()
#result = name.isdigit()#=> num
result = name.isalpha() #=> char 

#result = name.count("-")#=> count this character

#name=name.replace("-"," ")
print(result)
'''
############ indexing => accessing element of a sequence using [] 
#            [start : end : step]
'''
string="go to learn "
print(string[::2])
'''
############# while  loop => execute some code while some conditions remains true 
'''
name = input("enter your name : ")
while name=="":
    print(f"enter name {name}")
    name = input("enter your name : ")

'''

############ for loop => execute a block of code iteration numper 
#           you can iterate over range ,string ,sequance 


'''
#sss="123456"
for x in range(1,20):# reverced(range(1,11)) - range(1,11,2) - in sss
    if x==13:
        continue        ####### handel this and complete
    elif x== 16:
        break            ######## exit from loop 
    else:
        print(x)
'''
    
