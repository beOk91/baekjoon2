import sys
arr=[[0]*2 for i in range(41)]
arr[0][0],arr[1][1]=1,1
for i in range(2,41):
    arr[i][0]=arr[i-1][0]+arr[i-2][0]
    arr[i][1]=arr[i-1][1]+arr[i-2][1]
n=int(sys.stdin.readline().strip())

for _ in range(n):
    num=int(sys.stdin.readline().strip())
    print(arr[num][0],arr[num][1])