n=int(input())
for _ in range(n):
    a,b=input().strip().split()
    print("Distances: "+" ".join(str((ord(b)+26-ord(a))%26) for a,b in zip(a,b)))