import sys
t=int(sys.stdin.readline().strip())
for _ in range(t):
    t_list=list(map(int,sys.stdin.readline().strip().split()))
    print(sum(t_list))