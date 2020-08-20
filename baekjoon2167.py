n,m=map(int,input().strip().split())
arr=[[0]*m for _ in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().strip().split()))
k=int(input().strip())
for _ in range(k):
    i,j,x,y=map(int,input().strip().split())
    result=0
    for k in range(j-1,y):
        for l in range(i-1,x):
            result+=arr[l][k]
    print(result)