t=int(input())
arr=[0]*1001
arr[1]=1
for _ in range(t):
    n=int(input())
    if arr[n]!=0:print(arr[n])
    else:
        for i in range(2,n+1):
            arr[i]=arr[i-1]*i%10 if arr[i-1]*i%10!=0 else (arr[i-1]*i)//10%10
        print(arr[n])