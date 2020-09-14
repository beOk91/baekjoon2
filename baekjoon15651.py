def f(limit,arr1,arr2):
    if len(arr2)==limit:print(" ".join(str(i) for i in arr2));return
    for i in range(len(arr1)):
        f(limit,arr1,arr2+[arr1[i]])

n,m=map(int,input().strip().split())
arr=[i for i in range(1,n+1)]
f(m,arr,[])