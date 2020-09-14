import itertools,sys
n=int(sys.stdin.readline().strip())
n_list=sorted(list(map(int,sys.stdin.readline().strip().split())),reverse=True)
total=0
for i in range(n):
    for j in range(i+1):
        total+=(i-j)
print(total*2)

print(sum(abs(a-b) for a,b in list(itertools.combinations(n_list,2)))*2)