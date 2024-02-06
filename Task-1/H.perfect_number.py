num=int(input("enter num = "))

sum_of_proper_div=0

for i in range(1,int(num/2)+1):
    if num%i==0:
        sum_of_proper_div+=i
#print(sum_of_proper_div)
if num==sum_of_proper_div:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not A perfect number.")
