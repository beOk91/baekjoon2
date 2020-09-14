def f(idx,cnt,arr1,arr2):
    if len(arr2)==cnt:
        print(" ".join(str(element) for element in arr2));return
    if idx==len(arr1):return

    f(idx+1,cnt,arr1,arr2+[arr1[idx]])
    f(idx+1,cnt,arr1,arr2)

n,m=map(int,input().strip().split())
arr=[i for i in range(1,n+1)]
f(0,m,arr,[])