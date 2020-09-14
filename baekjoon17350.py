import sys
n=int(sys.stdin.readline().strip())
flag=False
for _ in range(n):
    text=sys.stdin.readline().strip()
    if text=="anj":
        flag=True
print("뭐야;" if flag else "뭐야?")