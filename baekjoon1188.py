import sys,math
n,m=map(int,sys.stdin.readline().strip().split())
lcm=n//math.gcd(n,m)*m
print((lcm//n-1)*n)