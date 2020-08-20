import math,sys
def f(n):
    if n==0 or n==1:
        return 1
    else:
        return n*f(n-1)
try:
    while True:
        n,k=map(int,sys.stdin.readline().strip().split())
        print(math.gcd(f(n),k))
except:
    exit()