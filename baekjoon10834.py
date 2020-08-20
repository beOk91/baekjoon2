n=int(input())
arr=[[0]*3 for _ in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().strip().split()))
for i in range(1,n):
    arr[i][2]+=arr[i-1][2]
    arr[i][1]=arr[i][1]*(arr[i-1][1]//arr[i][0])
    arr[i][0]=arr[i-1][1]

print(arr[n-1][2]%2,arr[n-1][1])