import math
n=int(input())
for _ in range(n):
    a,b=map(int,input().strip().split())
    ab_gcd=math.gcd(a,b)
    print(a*b//ab_gcd,ab_gcd)