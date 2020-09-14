n=int(input())
for _ in range(n):
    r,e,c=map(int,input().strip().split())
    print("advertise" if r<e-c else "does not matter" if r==e-c else "do not advertise")