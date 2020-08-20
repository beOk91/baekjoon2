a,b,c=map(int,input().strip().split())
arr=[0]*6
arr[a-1]+=1
arr[b-1]+=1
arr[c-1]+=1
for i in range(5,-1,-1):
    if arr[i]==3:
        arr[i]=10000+(i+1)*1000
    elif arr[i]==2:
        arr[i]=1000+(i+1)*100
    elif arr[i]!=0:
        arr[i]=(i+1)*100
print(max(arr))