arr=list(map(int,input().strip().split()))
arr2=list(map(int,input().strip().split()))
minVal=min(arr[0]//arr2[0],arr[1]//arr2[1],arr[2]//arr2[2])
for i in range(3):
    arr[i]-=minVal*arr2[i]
val=arr2[arr.index(min(arr))]
val2=min(arr2[i]/val for i in range(3))
if min(arr)!=0:
    for i in range(3):
        arr2[i]/=val
    print(" ".join("%.6f" %(a-b) if a-b!=0 else "0" for a,b in zip(arr,arr2)))
else:
    print(arr[0],arr[1],arr[2])