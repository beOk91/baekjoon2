n,m=map(int,input().strip().split())
n_list=[element for element in range(1,n+1)]
visited=[False]*n
result=[]
def f(arr):
    if len(arr)==m:
        result.append(arr)
        return 
    else:
        for i in range(n):
            if visited[i]:
                continue
            visited[i]=True
            f([n_list[i]]+arr)
            visited[i]=False            
f([])
result.sort()
print("\n".join(str(" ".join(str(i) for i in element)) for element in result))