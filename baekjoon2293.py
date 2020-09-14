n,k=map(int,input().strip().split())
n_list=[]
for _ in range(n):
    n_list.append(int(input().strip()))
dp=[1 if i%n_list[0]==0 else 0 for i in range(k+1)]
for i in range(1,n):
    for j in range(n_list[i],k+1):
        dp[j]+=dp[j-n_list[i]]
print(dp[k])