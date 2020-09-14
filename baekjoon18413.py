import sys
n,m=map(int,sys.stdin.readline().strip().split())
arr=[0]*(m+1)
n_list=list(map(int,sys.stdin.readline().strip().split()))
for element in n_list:
    arr[element]+=1
print(max(arr))