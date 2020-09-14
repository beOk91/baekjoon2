n=int(input())
dp=[0,1,2,3]+[0]*(n-3)
for i in range(3,n+1):
    dp[i]=(dp[i-1]+dp[i-2])%15746
print(dp[n])