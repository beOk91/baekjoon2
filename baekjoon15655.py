import sys
def f(idx,limit,arr,arr2):
    if len(arr2)==limit:
        print(" ".join(str(element) for element in arr2));return
    if idx==len(arr):return
    f(idx+1,limit,arr,arr2+[arr[idx]])
    f(idx+1,limit,arr,arr2)

n,m=map(int,sys.stdin.readline().strip().split())
n_list=sorted(list(map(int,sys.stdin.readline().strip().split())))
f(0,m,n_list,[])