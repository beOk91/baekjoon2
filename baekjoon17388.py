arr=list(map(int,input().strip().split()))
if sum(arr)>=100:
    print("OK")
else:
    print("Soongsil" if (arr[0]<arr[1] and arr[0]<arr[2]) else ("Korea" if (arr[1]<arr[0] and arr[1]<arr[2]) else ("Hanyang" if (arr[2]<arr[0] and arr[2]<arr[1]) else "hello")))