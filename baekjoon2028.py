t=int(input())
for _ in range(t):
    n=int(input())
    print("YES" if str(n**2)[len(str(n**2))-len(str(n)):len(str(n**2))]==str(n) else "NO")