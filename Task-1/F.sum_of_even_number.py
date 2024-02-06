intnum=int(input("enter a integr num = "))
sumofeven=0
numofeven=""
for x in range(1,intnum+1):
    if x<=intnum and x%2==0:
        sumofeven+=x
        if x==intnum-1 or x==intnum:
            numofeven+=f"{str(x)}"
        else:
            numofeven+=f"{str(x)} + "
    else:
        continue
        
print(f"The sum of even numbers from 1 to {intnum} is {sumofeven} ({numofeven}).")
