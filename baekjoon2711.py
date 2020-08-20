n=int(input())
for _ in range(n):
    a,b=input().strip().split()
    print(b[0:int(a)-1]+b[int(a):])