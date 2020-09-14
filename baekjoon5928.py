d,h,m=map(int,input().strip().split())
time=d*24*60+h*60+m-(11*24*60+11*60+11)
print(-1 if time<0 else time)