import sys
n,k=map(int,sys.stdin.readline().strip().split())
goods=[(0,0)]
for _ in range(n):
    w,v=map(int,sys.stdin.readline().strip().split())
    goods.append((w,v))
dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if j-goods[i][0]>=0:
            dp[i][j]=max(goods[i][1]+dp[i-1][j-goods[i][0]],dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j] 
print(dp[n][k])
