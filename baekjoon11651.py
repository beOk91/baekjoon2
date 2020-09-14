import sys
n=int(sys.stdin.readline().strip())
matrix=[]
for _ in range(n):
    matrix.append(list(map(int,sys.stdin.readline().strip().split())))
matrix.sort(key=lambda x:(x[1],x[0]))
print("\n".join((str(element[0])+" "+str(element[1])) for element in matrix))