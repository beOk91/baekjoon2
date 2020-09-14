n=int(input())
arr=[False,False]+[True]*(int(n**0.5)-1)
cnt=0
for i in range(2,len(arr)):
    for j in range(i+i,len(arr),i):
        if arr[j]:arr[j]=False
for i in range(len)