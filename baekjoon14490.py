import math
n,m=map(int,input().strip().split(":"))
while math.gcd(n,m)!=1:
    n,m=n//math.gcd(n,m),m//math.gcd(n,m)
print(str(n)+":"+str(m))