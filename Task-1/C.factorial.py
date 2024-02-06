num = int(input("enter positive numper : "))
fact = 1
if num==0:
    print("the fact = 1")
else:
    while num!=1:
        fact*=num
        num-=1

print(f"the fact = {fact}")
