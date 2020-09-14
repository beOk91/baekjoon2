n=int(input())
n_list=list(map(int,input().strip().split()))
n_list2=[0]*n
for i in range(1,n):
    for j in range(i):
        if n_list[j]<n_list[i]:n_list2[i]+=1
print(max(n_list2))