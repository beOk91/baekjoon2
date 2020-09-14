n,m=map(int,input().strip().split())
arr=[[0]*n for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().strip().split())
    arr[a-1][b-1]=1
    arr[b-1][a-1]=1
print("\n".join(str(sum(element)) for element in arr))