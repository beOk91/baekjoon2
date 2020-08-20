arr=[[0]*9 for i in range(9)]
for i in range(9):
    arr[i]=list(map(int,input().strip().split()))
max_x,max_y=0,0

for i in range(9):
    for j in range(9):
        if arr[i][j]>arr[max_x][max_y]:
            max_x=i
            max_y=j
print(arr[max_x][max_y])
print(max_x+1,max_y+1)