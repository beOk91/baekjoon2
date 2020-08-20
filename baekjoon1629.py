import sys
a,b,c=map(int,sys.stdin.readline().strip().split())
result=1
for _ in range(b):
    result*=a
print(result%12)