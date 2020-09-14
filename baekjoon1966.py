import collections
t=int(input())
for _ in range(t):
    n,m=map(int,input().strip().split())
    n_list=list(map(int,input().strip().split()))
    n_list=collections.deque([(i1,i2) for i1,i2 in enumerate(n_list)])
    cnt=0
    while True:
        if n_list[0]==max(n_list,key=lambda x:x[1]):
            cnt+=1
            idx=n_list.popleft()[0]
            if idx==m:print(cnt);break
        else:
            n_list.append(n_list.popleft())