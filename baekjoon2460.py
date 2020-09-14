result=[0]*10
for i in range(10):
    arr=list(map(int,input().strip().split()))
    if i==0:result[i]=-arr[0]+arr[1]
    else:result[i]=result[i-1]-arr[0]+arr[1]
print(max(result))