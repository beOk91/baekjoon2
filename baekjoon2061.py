import sys
p,k=map(int,sys.stdin.readline().strip().split())
arr=[False,False]+[True]*(k-1)
for i in range(2,int(k**0.5)+1):
    for j in range(i+i,k+1,i):
        if arr[j]:arr[j]=False
for i in range(2,k+1):
    if i==k:
        print("GOOD");break
    if arr[i]:
        if p%i==0:
            print("BAD", str(i));break
