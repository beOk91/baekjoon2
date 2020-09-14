m,n=map(int,input().strip().split())
arr=[True]*(n+1)
arr[0],arr[1]=False,False
for i in range(2,int(n**0.5)+1):
    if arr[i]:
        for j in range(i+i,n+1,i):
            arr[j]=False
print("\n".join(str(i) for i in range(m,len(arr)) if arr[i]))