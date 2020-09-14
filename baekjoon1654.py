import sys
k,n=map(int,sys.stdin.readline().strip().split())
k_list=[]
for _ in range(k):
    k_list.append(int(sys.stdin.readline().strip()))
start,end=1,max(k_list)
while start<=end:
    mid=(start+end)//2
    print(start,end,mid)
    total=0
    for k1 in k_list:
        total+=(k1//mid)
    if total<n:end=mid-1
    else:start=mid+1
print(end)