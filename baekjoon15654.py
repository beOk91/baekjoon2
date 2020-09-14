import sys
def f(limit,arr,arr2):
    if len(arr2)==limit:
        print(" ".join(str(element) for element in arr2));return
    for i in range(len(arr)):
        if visited[i]:
            visited[i]=False
            f(limit,arr,arr2+[arr[i]])
            visited[i]=True

n,m=map(int,sys.stdin.readline().strip().split())
n_list=sorted(list(map(int,sys.stdin.readline().strip().split())))
visited=[True]*(n+1)
f(m,n_list,[])