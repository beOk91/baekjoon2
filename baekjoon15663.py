import sys
def f(limit,arr1,arr2):
    if len(arr2)==limit:
        result.add(" ".join(str(arr2[i]) for i in range(len(arr2))))
    for i in range(len(arr1)):
        if visited[i]:
            visited[i]=False
            f(limit,arr1,arr2+[arr1[i]])
            visited[i]=True

n,m=map(int,sys.stdin.readline().strip().split())
n_list=list(map(int,sys.stdin.readline().strip().split()))
visited=[True]*(n+1)
result=set([])
f(m,n_list,[])
result=sorted(list(map(int,element.strip().split())) for element in list(result))
print("\n".join(" ".join(str(i) for i in element) for element in result))
"""
result=list(set(result))
for i in range(len(result)):
    result2.append(list(map(int,result[i].strip().split())))
result2.sort()
print("\n".join(" ".join(str(i) for i in element) for element in result2))
"""