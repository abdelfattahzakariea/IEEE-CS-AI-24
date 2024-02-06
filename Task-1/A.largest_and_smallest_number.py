x = int(input("enter new numper : "))
minmum = 100000000000
maxmum =-100000000000
while x!=-1:
    minmum = min(x,minmum)
    maxmum = max(x,maxmum)
    x=int(input("enter new numper : "))


print(f"maxmum numper = {maxmum}")
print(f"minmum numper = {minmum}")
