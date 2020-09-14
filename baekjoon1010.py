t=int(input())
for _ in range(t):
    n,m=map(int,input().strip().split())
    result=1
    for i in range(m,m-n,-1):
        result*=i
    for i in range(n,0,-1):
        result/=i
    print(int(result))