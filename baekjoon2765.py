n=1
while True:
    a=list(map(float,input().strip().split()))
    if a[1]==0:
        break
    print("Trip #%d: %.2f %.2f" %(n,round(a[0]*3.1415927*a[1]/12/5280,2),round(a[0]*3.1415927*a[1]/12/5280*3600/a[2],2)))
    n+=1