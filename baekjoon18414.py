x,l,r=map(int,input().strip().split())
arr=[0]*(r-l+1)
for i in range(l,r+1):
    arr[i-l]=abs(i-x)
print(arr.index(min(arr))+l)