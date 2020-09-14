a,b,n=map(int,input().strip().split())
for i in range(n):
    a%=b
    a*=10
print(int(a//b))