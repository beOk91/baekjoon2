n=int(input().strip())
dp=[1,1]+[0]*n
for i in range(2,n+1):
    for j in range(i):
        dp[i]+=(dp[j]*dp[i-j-1])
print(dp[n])