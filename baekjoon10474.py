while True:
    a,b=map(int,input().strip().split())
    if a==0 and b==0:
        break
    else:
        print(str(a//b),str(a%b),"/",b)