n,k=map(int,input().strip().split())
pascal=[[0] * (i+1) for i in range(n)]
pascal[0][0]=1
for i in range(1,n):
    for j in range(len(pascal[i])):
        if j==0 or i==j:
            pascal[i][j]=1
        else:
            pascal[i][j]=pascal[i-1][j-1]+pascal[i-1][j]
print(pascal[n-1][k-1])