a,b=map(int,input().strip().split())
a,b=b if b<a else a,a if a>b else b
if a>=0 and b>=0:
    print(b*(b+1)//2-(a-1)*a//2)
elif a<0 and b>=0:
    a*=-1
    print(-a*(a+1)//2+b*(b+1)//2)
elif a<0 and b<0:
    a*=-1
    b*=-1
    print((a*(a+1)//2-(b-1)*b//2)*-1)