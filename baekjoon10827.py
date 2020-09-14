a,b=map(float,input().strip().split())
print(a**int(b))
ret=1
for i in range(int(b)):
    ret*=a
print(ret)