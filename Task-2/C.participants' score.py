maxx = -1000000000000
xx=int(input())
arr=input()
arr=arr.split()
arr = [int(num) for num in arr]

for x in range(0, xx):
    maxx=max(maxx, arr[x])
for x in range(0, arr.count(maxx)):
    arr[arr.index(maxx)]=-1000
maxx=-100000000000000
for x in range(0, len(arr)):
    maxx=max(maxx, arr[x])
print(maxx)
