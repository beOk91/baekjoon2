import sys
n=int(sys.stdin.readline().strip())
result=0
for _ in range(n):
    result+=(int(sys.stdin.readline().strip())-1)
print(result+1)