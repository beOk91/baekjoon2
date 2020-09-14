import sys
n,m=map(int,sys.stdin.readline().strip().split())
m=[[0]*m for _ in range(n)]
for i in range(n):
    m[i]=list(map(int,sys.stdin.readline().strip().split()))
k=int(sys.stdin.readline().strip())
for _ in range(k):
    i,j,x,y=map(int,sys.stdin.readline().strip().split())
    result=0
    for l in range(i-1,x):
        result+=sum(m[i-1:x][j-1:y])
    print(result)