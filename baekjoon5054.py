t=int(input())
for _ in range(t):
    n=int(input())
    n_list=list(map(int,input().strip().split()))
    print((max(n_list)-min(n_list))*2)