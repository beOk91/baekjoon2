t=int(input())
for _ in range(t):
    n=int(input())
    arr=[0]*2
    for _ in range(n):
        a,b=input().strip().split()
        arr[0]+=int(a)
        arr[1]+=(int(a)*float(b))
    print("%d %.1f" %(arr[0],arr[1]/arr[0]))