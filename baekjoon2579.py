import sys
n=int(sys.stdin.readline().strip())
stairs=[int(sys.stdin.readline().strip()) for _ in range(n)]
dp=[0]*n
for i in range(n):
    if i==0:
        dp[0]=stairs[i]
    elif i==1:
        dp[1]=stairs[0]+stairs[i]
    elif i==2:
        dp[2]=max(stairs[0]+stairs[i],stairs[1]+stairs[i])
    else:
        dp[i]=max(dp[i-2]+stairs[i],dp[i-3]+stairs[i-1]+stairs[i])
print(dp[n-1])