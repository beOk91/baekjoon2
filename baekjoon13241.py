import math
a,b=map(int,input().strip().split())
ab_gcd=math.gcd(a,b)
print(a*b//ab_gcd)