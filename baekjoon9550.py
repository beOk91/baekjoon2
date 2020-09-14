t=int(input())
for _ in range(t):
    n,k=map(int,input().strip().split())
    n_list=list(map(int,input().strip().split()))
    print(0 if max(n_list)<k else sum([element//k for element in n_list]))