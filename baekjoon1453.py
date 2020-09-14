arr,cnt=[True]*101,0
n=int(input())
n_list=list(map(int,input().strip().split()))
for i in range(n):
    if arr[n_list[i]]:arr[n_list[i]]=False
    else:cnt+=1
print(cnt)