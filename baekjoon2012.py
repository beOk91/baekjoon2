import sys
n=int(sys.stdin.readline().strip())
rank=[]
for _ in range(n):
    rank.append(int(sys.stdin.readline().strip()))
rank.sort()
total=0
for i in range(1,n+1):
    total+=abs(rank[i-1]-i)
print(total)