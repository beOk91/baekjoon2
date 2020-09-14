import sys
n=int(sys.stdin.readline().strip())
"""
dp=[0,3,7,17,41]+[0]*n
for i in range(3,n+1):
    dp[i]=(dp[i-1]*2+dp[i-2])%9901
print(dp[n])
"""
dp=[1,1,1]
for i in range(1,n):
    dp[0],dp[1],dp[2]=dp[0]+dp[1]+dp[2],dp[0]+dp[2],dp[0]+dp[1]
print(sum(dp)%9901)