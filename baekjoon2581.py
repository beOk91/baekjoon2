import sys
m=int(sys.stdin.readline().strip())
n=int(sys.stdin.readline().strip())
arr=[False,False]+[True]*(n+1)
for i in range(2,n+1):
    for j in range(i+i,n+1,i):
        if arr[j]:
            arr[j]=False
result=0+sum(i if arr[i] else 0 for i in range(m,n+1))
print(result if result!=0 else -1)
if result!=0:
    for i in range(m,n+1):
        if arr[i]:print(i);break