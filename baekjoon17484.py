n,m=map(int,input().strip().split())
arr=[[0]*m for _ in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().strip().split()))
for i in range(1,n):
    for j in range(m):
        if j==0:arr[i][j]=arr[i][j]+arr[i-1][j+1]
        elif j==m-1:arr[i][j]=arr[i][j]+arr[i-1][j-1]
        else:arr[i][j]=arr[i][j]+min(arr[i-1][j-1],arr[i-1][j+1])
print(min(arr[n-1]))