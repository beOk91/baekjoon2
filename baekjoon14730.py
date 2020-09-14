import sys
n=int(sys.stdin.readline().strip())
total=0
for _ in range(n):
    c,k=map(int,sys.stdin.readline().strip().split())
    total+=c*k
print(total)