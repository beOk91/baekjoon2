a,b=map(int,input().strip().split())
arr=[False,False]+[True if str(element)==str(element)[::-1] else False for element in range(2,b+1)]
for i in range(2,b+1):
    for j in range(i+i,b+1,i):
        if arr[j]:arr[j]=False
print("\n".join(str(element) for element in range(a,b+1) if arr[element] and str(element)==str(element)[::-1]))
print(-1)