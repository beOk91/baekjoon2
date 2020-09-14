n=int(input())
rgb=[[0]*3 for _ in range(n)]
for i in range(n):
    rgb[i]=list(map(int,input().strip().split()))
for i in range(1,n):
    for j in range(3):
        temp=rgb[i-1][0:j]+rgb[i-1][j+1:]
        rgb[i][j]=rgb[i][j]+min(temp)
print(min(rgb[n-1]))