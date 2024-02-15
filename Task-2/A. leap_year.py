def is_leap(year):
    leap = False
    
    while year>100:
        if year %100==0:
            year/=100
        else:
            break
    if year%4==0:
        return not leap
    else:
        return leap

year = int(input())
print(is_leap(year))

