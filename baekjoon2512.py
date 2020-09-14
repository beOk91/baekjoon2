import sys
n=int(sys.stdin.readline().strip())
n_list=sorted(list(map(int,sys.stdin.readline().strip().split())))
m=int(sys.stdin.readline().strip())
start,end=0,n_list[-1]

if sum(n_list)<=m:
    print(max(n_list))
else:
    while start<=end:
        mid=(start+end)//2
        budget=0
        for n in n_list:
            budget+=min(n,mid)
        if budget>m:
            end=mid-1
            mid=end
        else:
            start=mid+1
    print(mid)