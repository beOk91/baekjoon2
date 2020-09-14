import sys
n,m=map(int,sys.stdin.readline().strip().split())
pokedex={}
for i in range(1,n+1):
    name=sys.stdin.readline().strip()
    pokedex[name]=i
    pokedex[str(i)]=name
for _ in range(m):
    q=sys.stdin.readline().strip()
    print(pokedex[q])