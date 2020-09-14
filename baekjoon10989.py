import sys
num=int(sys.stdin.readline().strip())
arr=[]
for _ in range(num):
    arr.append(int(sys.stdin.readline().strip()))
arr.sort()
print("\n".join(str(i) for i in arr))