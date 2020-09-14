import sys
t=int(sys.stdin.readline().strip())
for _ in range(t):
    n=int(sys.stdin.readline().strip())
    n_list=list(map(int,sys.stdin.readline().strip().split()))
    print("Equilibrium" if sum(n_list)==0 else "Right" if sum(n_list)>0 else "Left")