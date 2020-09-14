import sys
n,m=map(int,sys.stdin.readline().strip().split())
l={}
cnt=[]
for _ in range(n):
    l[sys.stdin.readline().strip()]=1
for _ in range(m):
    name=sys.stdin.readline().strip()
    if l.get(name,0)==1:cnt.append(name)
cnt.sort()
print(len(cnt));print("\n".join(str(e) for e in cnt))