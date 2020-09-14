import sys
n=int(sys.stdin.readline().strip())
arr=[[0]*n for _ in range(n)]
for i in range(n):
    arr[i]=list(map(int,sys.stdin.readline().strip().split()))