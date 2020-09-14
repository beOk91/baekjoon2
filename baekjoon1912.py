n=int(input())
n_list=list(map(int,input().strip().split()))
result=[n_list[0]]+[0]*(len(n_list)-1)
for i in range(1,len(n_list)):
    result[i]=max(result[i-1]+n_list[i],n_list[i])
print(max(result))