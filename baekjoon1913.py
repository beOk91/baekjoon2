import sys
n=int(sys.stdin.readline().strip())
f=int(sys.stdin.readline().strip())
num=n*n
arr=[[0]*n for _ in range(n)]
x,y,arr[x][y],snail_num,direction=n//2,n//2,1,2,"up"
while snail_num!=n*n+1:
    if direction=="up" and arr[x-1][y]==0:
        x-=1
        arr[x][y]=snail_num
        if arr[x][y+1]==0:
            direction="right"
    elif direction=="right" and arr[x][y+1]==0:
        y+=1
        arr[x][y]=snail_num
        if arr[x+1][y]==0:
            direction="down"
    elif direction=="down" and arr[x+1][y]==0:
        x+=1
        arr[x][y]=snail_num
        if arr[x][y-1]==0:
            direction="left"
    elif direction=="left" and arr[x][y-1]==0:
        y-=1
        arr[x][y]=snail_num
        if arr[x-1][y]==0:
            direction="up"
    snail_num+=1
    
f_x,f_y=0,0
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
        if f==arr[i][j]:f_x=i;f_y=j
    print()
print(f_x+1,f_y+1)