n=int(input())
n_list=list(map(int,input().strip().split()))
cnt=0
print(sum(1 if n_list[i]!=(i+1) else 0 for i in range(n)))
