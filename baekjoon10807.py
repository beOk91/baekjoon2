n=int(input())
n_list=list(map(int,input().strip().split()))
arr,arr2=[0]*101,[0]*101
for element in n_list:
    if element<0:arr2[element]+=1
    else:arr[element]+=1
v=int(input())
print(arr[v] if v>=0 else arr2[v])