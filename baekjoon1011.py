n=int(input())
for _ in range(n):
    a,b=map(int,input().strip().split())
    a,b=a-a,b-a
    cnt=0
    while cnt!=b:
        if cnt==0:
            cnt+=1
        