import sys
n=int(sys.stdin.readline().strip())
n_list=list(map(int,sys.stdin.readline().strip().split()))
line=[]
for i in range(1,n+1):
    line.insert(n_list[i-1],i)
line=line[::-1]
print(" ".join(str(e) for e in line))