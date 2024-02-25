import math

def get_numbers(numper):
    list=[]
    
    for num in range(0,numper):
        try:
            push_num=int(input("enter num : "))
            list.append(push_num)
        except ValueError:
            push=int(input("enter integr numper :"))
            list.append(push)
    return list
        
def find_min(numbers):
    return min(numbers)


def find_max(numbers):
    return max(numbers)


def find_mean(numbers):
    sum_of_num=0
    for number in range(0,len(numbers)):
        sum_of_num+=numbers[number]
    mean=sum_of_num/len(numbers)
    return mean


def find_mode(numbers):
    freq=dict()
    mode=[]
    for number in numbers:
        freq[number]=freq.get(number,0) + 1
    
    maxmum_freq=max(freq.values())
    for key, value in freq.items():
        if value==maxmum_freq:
            mode.append(key)
    return mode

def find_median(numbers):
    median=0
    length=int(len(numbers))
    numbers.sort()
    
    if length%2 == 0:
        median=((numbers[int(length/2)-1]+numbers[int(length/2)])/2)
    else:
        median=numbers[int(length/2)]    
    
    return median


def find_range(numbers):
    range=(max(numbers)-min(numbers))
    return range
def find_variance(numbers):
    mean=find_mean(numbers)
    summtion = 0
    for num in range(0,len(numbers)):
        summtion += (numbers[num]-mean)**2
    
    variance=round(float(summtion/len(numbers)),2)
    return variance

def find_STD(numbers):
    var=find_variance(numbers)
    Std=round(math.sqrt(var),5)
    return Std

def find_Quariles(numbers):
    quartails=()
    numbers.sort()
    length=len(numbers)
    place_q1=int(length/4)

    if length%2 == 0:
        q1=numbers[int(place_q1)]
        q3=numbers[-int(place_q1  + 1)]
        q2=find_median(numbers)
    else:
        q1=(numbers[place_q1-1]+numbers[place_q1])/2
        q3=(numbers[-(place_q1+1)]+numbers[-(place_q1)])/2
        q2= find_median(numbers)
    quartails=(q1,q2,q3)
    return quartails

def find_IQR(numbers):
    quartilss=find_Quariles(numbers)
    iqr=quartilss[2]-quartilss[0]
    return iqr