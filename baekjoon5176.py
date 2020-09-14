k=int(input())
for _ in range(k):
    p,m=map(int,input().strip().split())
    seat,cnt=[False]*501,0
    for i in range(p):
        j=int(input().strip())
        if not seat[j]:seat[j]=True
        else:cnt+=1
    print(cnt)