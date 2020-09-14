import sys
n,k=map(int,sys.stdin.readline().strip().split())
n_list=sorted(list(map(int,sys.stdin.readline().strip().split())))
print(n_list[k-1])