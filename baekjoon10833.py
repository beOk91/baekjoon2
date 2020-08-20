n=int(input())
result=0
for _ in range(n):
    a,b=map(int,input().strip().split())
    result+=b%a
print(result)