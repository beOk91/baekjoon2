n,w,h=map(int,input().strip().split())
for _ in range(n):
    a=int(input())
    print("DA" if a<=(w**2+h**2)**0.5 else "NE")