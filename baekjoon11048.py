n,m=map(int,input().strip().split())
candy=[[0]*m for _ in range(n)]
dp=[[0]*m for _ in range(n)]
for i in range(n):
    candy[i]=list(map(int,input().strip().split()))

for i in range(n):
    for j in range(m):
        dp[i][j]+=candy[i][j]
        if i>=1 and j>=1:
            dp[i][j]=candy[i][j]+max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        elif j==0  and i>=1:
            dp[i][j]+=dp[i-1][j]
        elif i==0 and j>=1:
            dp[i][j]+=dp[i][j-1]

print(dp[n-1][m-1])
