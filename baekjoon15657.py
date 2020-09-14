import sys
def f(limit,arr,arr2):
    if len(arr2)==limit:
        print(" ".join(str(element) for element in arr2));return
    for i in range(len(arr)):
        if len(arr2)==0 or arr2[-1]<=arr[i]:
            f(limit,arr,arr2+[arr[i]])
n,m=map(int,sys.stdin.readline().strip().split())
n_list=sorted(list(map(int,sys.stdin.readline().strip().split())))
f(m,n_list,[])
