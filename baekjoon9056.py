t=int(input())
for _ in range(t):
    a,b=input().strip().split()
    for i in range(len(a)-1):
        b[b.index(a[i]):]