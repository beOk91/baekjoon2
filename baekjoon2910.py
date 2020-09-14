n,c=map(int,input().strip().split())
n_list=list(map(int,input().strip().split()))
arr=[0]*(c+1)
for e in n_list:
    arr[e]+=1
arr2=sorted(arr.copy(),reverse=True)
print(arr)
print(arr2)
print(" ".join(" ".join(str(arr.index(element)) for _ in range(element)) for element in arr2 if element!=0))
