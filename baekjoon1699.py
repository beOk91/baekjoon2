import sys
n=int(sys.stdin.readline().strip())
dp=[i for i in range(n+1)]
for j in range(2,int(n**0.5)+1):
    for k in range(j**2,n+1):
        if dp[k]>dp[k-j*j]+1:
            dp[k]=dp[k-j*j]+1
print(dp[n])