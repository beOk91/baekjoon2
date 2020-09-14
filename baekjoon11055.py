n=int(input())
n_list=list(map(int,input().strip().split()))
dp=[1]*n
dp2=[[] for _ in range(n)]
for i in range(n):
    for j in range(i):
        if n_list[i]>n_list[j] and dp[i]<dp[j]+1:
            dp[i]+=1
            dp2[i].append(n_list[j])
    if dp[i]>dp[i-1]:
        dp2[i]=list(dp2[i-1])
    dp2[i].append(n_list[i])
print(dp)
print(dp2)
print(sum(dp2[dp.index(max(dp))]))

"""
10
100 110 90 80 70 80 90 1 2 3
"""