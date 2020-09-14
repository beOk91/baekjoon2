import sys
n=int(sys.stdin.readline().strip())
for _ in range(n):
    text=sys.stdin.readline().strip().upper()
    print("Yes" if text==text[::-1] else "No")