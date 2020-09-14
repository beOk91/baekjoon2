n=int(input())
n_list=list(map(int,input().strip().split()))
dp=[-1]*n
def f(start):
    for i in range(n):
        dp[i]=1
        for j in range(i):
            if n_list[i]>n_list[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)
print(f(0))
