n=int(input())
for _ in range(n):
    a,b=input().strip().split()
    print(int(str(int(a[::-1])+int(b[::-1]))[::-1]))