n=int(input())
n_list=list(map(int,input().strip().split()))
result=[0]*n
for i in range(n):
    cnt=0
    for j in range(i+1,n):
        if n_list[j]>n_list[j-1]:
            cnt+=(n_list[j]-n_list[j-1])
        else:break
    result[i]=cnt
print(max(result))