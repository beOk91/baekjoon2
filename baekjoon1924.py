dayof2017=[31,28,31,30,31,30,31,31,30,31,30,31]
dayoftheweek=["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month,day=map(int,input().strip().split())
result=0
for i in range(month-1):
    result+=dayof2017[i]
result+=day
print(dayoftheweek[result%7])