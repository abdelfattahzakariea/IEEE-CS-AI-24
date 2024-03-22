count=[0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

countt = []
sum_of_list = 0
        
for k in range(256):
    for times in range(count[k]):
        countt.append(k)

length = len(countt)
minmum = countt[0]
maxmum = countt[length-1]
for i in countt:
    sum_of_list += i
mean = float(sum_of_list / length)

freq = {}
maximum_freq=0
mode = None
for number in countt:
    freq[number] = freq.get(number, 0) + 1
    if freq[number] > maximum_freq:
        maximum_freq = freq[number]
        mode = float(number)

if length % 2 == 0:
        median = float((countt[length // 2 - 1] + countt[length // 2]) / 2)
else:
    median = float(countt[length // 2])

if countt:
    result = [
        float(minmum),
        float(maxmum),
        mean,
        median,
        mode
        ]
    print(result)
else:
    print([])


'''
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        countt = []
        sum_of_list = 0
        
        for k in range(256):
            for times in range(count[k]):
                countt.append(k)
        
        length = len(countt)
        minmum = countt[0]
        maxmum = countt[length-1]
        for i in countt:
            sum_of_list += i
        mean = float(sum_of_list / length)

        freq = {}
        maximum_freq=0
        mode = None
        for number in countt:
            freq[number] = freq.get(number, 0) + 1
            if freq[number] > maximum_freq:
                maximum_freq = freq[number]
                mode = number

        if length % 2 == 0:
            median = float((countt[length // 2 - 1] + countt[length // 2]) / 2)
        else:
            median = float(countt[length // 2])

        if countt:
            result = [
                float(minmum),
                float(maxmum),
                mean,
                median,
                mode
                ]
            return result
        else:
            return []
'''