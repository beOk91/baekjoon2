n,k=map(int,input().strip().split())
arr=[False,False]+[True] * (n-1)
cnt=0
while cnt!=k:
    minVal=arr.index(True)
    for i in range(minVal,n+1,minVal):
        if arr[i]:
            arr[i]=False;cnt+=1
            if cnt==k:print(i);break
    if cnt==k:break