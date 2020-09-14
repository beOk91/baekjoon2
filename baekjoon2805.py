import sys
n,m=map(int,sys.stdin.readline().strip().split())
n_list=list(map(int,sys.stdin.readline().strip().split()))
start,end=0,max(n_list)
while start<=end:
    mid=(start+end)//2
    total=sum([(e-mid) if e>=mid else 0 for e in n_list])
    if total>=m:
        start=mid+1
    else:end=mid-1
print(end)