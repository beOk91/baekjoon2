import sys
n=int(sys.stdin.readline().strip())
for _ in range(n):
    a,b=map(int,sys.stdin.readline().strip().split())
    print((a**(b%4))%10 if a!=10 else 10)