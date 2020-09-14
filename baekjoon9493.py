while True:
    m,a,b=map(int,input().strip().split())
    if m==0 and a==0 and b==0:
        break
    time=round(m*60*60/a-m*60*60/b)
    print("%d:%02d:%02d" %(time//3600,time%3600//60,time%3600%60))