import sys
n=int(sys.stdin.readline().strip())
b=list(map(int,sys.stdin.readline().strip().split()))
for i in range(1,n+1):
    b[i-1]=b[i-1]*i
for i in range(n-1,0,-1):
    b[i]-=b[i-1]
print(" ".join(str(e) for e in b))