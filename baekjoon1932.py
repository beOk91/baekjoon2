n=int(input())
arr=[[0]*i for i in range(1,n+1)]
arr_sum=[[0]*i for i in range(1,n+1)]
for i in range(n):
    arr[i]=list(map(int,input().strip().split()))
arr_sum[0][0]=arr[0][0]
for i in range(1,n):
    for j in range(len(arr[i])):
        if j==0:
            arr_sum[i][j]=arr_sum[i-1][j]+arr[i][j]
        elif j==len(arr[i])-1:
            arr_sum[i][j]=arr_sum[i-1][i-1]+arr[i][j]
        else:
            arr_sum[i][j]=arr[i][j]+max(arr_sum[i-1][j-1],arr_sum[i-1][j])
print(max(arr_sum[n-1]))