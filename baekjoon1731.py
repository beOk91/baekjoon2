import sys
n=int(sys.stdin.readline().strip())
arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))
if arr[1]-arr[0]== arr[2]-arr[1]:
    print(arr[-1]+arr[1]-arr[0])
else:
    print(arr[-1]*arr[1]//arr[0])