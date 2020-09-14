dayof2009=[31,28,31,30,31,30,31,31,30,31,30,31]
dayoftheweek=["Wednesday","Thursday", "Friday", "Saturday", "Sunday","Monday", "Tuesday" ]
d,m=map(int,input().strip().split())
print(dayoftheweek[(sum(dayof2009[i] for i in range(m-1))+d)%7])