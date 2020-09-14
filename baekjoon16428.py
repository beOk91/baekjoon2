a,b=map(int,input().strip().split())
if b<0:
    r=a//b if a%b==0 else a//b+1
    print(r)
    print(a-r*b)
else:
    print(a//b)
    print(a-a//b*b)
