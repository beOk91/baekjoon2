n=int(input())
p1,p2=100,100
for _ in range(n):
    a,b=map(int,input().strip().split())
    if a>b:p2-=a
    elif a<b:p1-=b
print(p1)
print(p2)