import sys
def f(idx,limit,arr1,arr2):
    if len(arr2)==limit:
        result.add(" ".join(str(i) for i in arr2));return
    if idx==len(arr1):return
    f(idx+1,limit,arr1,arr2+[arr1[idx]])
    f(idx+1,limit,arr1,arr2)
n,m=map(int,sys.stdin.readline().strip().split())
n_list=sorted(list(map(int,sys.stdin.readline().strip().split())))
result=set([])
f(0,m,n_list,[])
result=sorted(list(map(int,element.strip().split())) for element in result)
print("\n".join(" ".join(str(i) for i in element) for element in result))