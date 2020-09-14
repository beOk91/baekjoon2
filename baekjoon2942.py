import math
r,g=map(int,input().strip().split())
for i in range(1,math.gcd(r,g)+1):
    if r%i==0 and g%i==0:
        print(i,r//i,g//i)