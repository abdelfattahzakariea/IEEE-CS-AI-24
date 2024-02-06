x=int(input("enter num = "))
s=""
y=0
for i in range(2,int(x/2)):
    if x==1:
        break
    while x%i==0:
        x/=i
        y+=1
        if y==1:
            s+=str(i)
        elif y==1001:
            s+=f", {str(i)}"
    if y!=0: 
        y=1000
if x!=1 and y!=0:
    s+=f", {int(x)}"
elif x!=1:
    s+=f"{x}"

print(f"Prime Factors: {s} ")
