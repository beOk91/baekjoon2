n=int(input())
dp=[1,3,5]+[0]*n
for i in range(3,n):
    dp[i]=(dp[i-1]+dp[i-2]*2)%10007
print(dp[n-1])