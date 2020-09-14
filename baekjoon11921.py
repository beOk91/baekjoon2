import sys
n=int(sys.stdin.readline().strip())
total=0
for _ in range(n):
    total+=int(sys.stdin.readline().strip())
print(str(n)+"\n"+str(total))