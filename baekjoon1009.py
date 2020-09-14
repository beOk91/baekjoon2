import sys
arr=[[0],[1],[6,2,4,8],[1,3,9,7],[6,4],[5],[6],[1,7,9,3],[6,8,4,2],[1,9],[10]]
n=int(sys.stdin.readline().strip())
for _ in range(n):
    a,b=map(int,sys.stdin.readline().strip().split())
    a=int(str(a)[-1]) if a%10!=0 else 10
    print(arr[a][b%len(arr[a])])