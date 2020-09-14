def inputNum(number,arr):
    if number>=len(arr)*len(arr)-1:return
    x,y,flag=0,0,False
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==-1:
                x,y=i,j;flag=True;break
        if flag:break
    arr[x][y],arr[x][y+1]=number,number+1
    arr[x+1][y],arr[x+1][y+1]=number+2,number+3
    number+=4
    inputNum(number,arr)

N,r,c=map(int,input().strip().split())
arr1=[[-1]*(2**N) for _ in range(2**N)]
inputNum(0,arr1)
print(arr1[r][c])
