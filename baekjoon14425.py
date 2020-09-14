import sys
n,m=map(int,sys.stdin.readline().strip().split())
s={}
cnt=0
for _ in range(n):
    s[sys.stdin.readline().strip()]=1
for _ in range(m):
    check_s=sys.stdin.readline().strip()
    if s.get(check_s,0)==1:
        cnt+=1
print(cnt)