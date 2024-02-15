name=[]
score=[]
index=[]
output=[]

minn=1000
for x in range(int(input())):
        name.append(input())
        score.append(float(input()))
        minn=min(minn,score[x])
        #concat=[name,score]
        #result.append(concat)
for _ in range(score.count(minn)):
    score[score.index(minn)]=100000

minn=1000
for x in range(0,len(score)):
    minn=min(score[x],minn)
for __ in range(score.count(minn)):
    index.append(score.index(minn))
    score[score.index(minn)]=1000
for x in range(0,len(index)):
    output.append(name[index[x]])
output.sort()

for x in range(0,len(output)):
    print(output[x])