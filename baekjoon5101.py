while True:
    arr=list(map(int,input().strip().split()))
    if arr[0]==0 and arr[0]==arr[1] and arr[1]==arr[2]:
        break
    print("X" if (arr[0]>arr[2] and arr[1]>0) or (arr[0]<arr[2] and arr[1]<0) else (arr[2]-arr[0])//arr[1]+1 if (arr[2]-arr[0])%arr[1]==0 else "X")