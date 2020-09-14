t=int(input())
p=[0,1,1,1,2,2,3,4,5,7,9]+[0]*91
for _ in range(t):
    n=int(input().strip())
    if p[n]!=0:print(p[n])
    else:
        for i in range(4,n+1):
            p[i]=p[i-2]+p[i-3]
        print(p[n])
