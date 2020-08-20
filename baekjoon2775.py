n=int(input())
for _ in range(n):
    a=int(input())
    b=int(input())
    sum1=0
    arr=[[0]*(b) for i in range(a+1)]
    for i in range(b):
        arr[a][i]=i+1
    for i in range(a-1,-1,-1):
        for j in range(b):
            for k in range(j+1):
                arr[i][j]+=arr[i+1][k]
    print(arr[0][b-1])