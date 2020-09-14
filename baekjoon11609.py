import sys
n=int(sys.stdin.readline().strip())
names=[]
for _ in range(n):
    names.append(sys.stdin.readline().strip())
names.sort(key=lambda x:(x.split()[1],x.split()[0]))
print("\n".join(e for e in names))