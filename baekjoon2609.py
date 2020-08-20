def gcd(a,b):
    if b!=0:
        return gcd(b,a%b)
    else:
        return a
a,b=map(int,input().strip().split())
a,b=b if b>=a else a,a if b>=a else b
print(gcd(a,b))
print(a//gcd(a,b)*b)
for i in range(b,0,-1):
    if a%i==0 and b%i==0:
        print(i)
        print(a//i*b)
        break