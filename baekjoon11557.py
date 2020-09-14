t=int(input())
for _ in range(t):
    n=int(input().strip())
    name,amt=[],[]
    for _ in range(n):
        n,a=input().strip().split()
        name.append(n)
        amt.append(int(a))
    print(name[amt.index(max(amt))])