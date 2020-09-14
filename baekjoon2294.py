n,k=map(int,input().strip().split())
n_list=[]
for _ in range(n):
    n_list.append(int(input().strip()))
n_list.sort()
dp=[i//n_list[0] if i%n_list[0]==0 else -1 for i in range(k+1)]
for i in range(1,n):
    for j in range(n_list[i],k+1):
        if j%n_list[i]==0:
            dp[j]=j//n_list[i]
        dp[j]=min(dp[j] if dp[j]!=-1 else dp[j-n_list[i]]+1,dp[j-n_list[i]]+1 if dp[j-n_list[i]]!=-1 else dp[j])
print(dp[k])