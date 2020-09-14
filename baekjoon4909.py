while True:
    arr=list(map(int,input().strip().split()))
    if sum(arr)==0:
        break
    arr.remove(max(arr))
    arr.remove(min(arr))
    print(sum(arr)/len(arr) if sum(arr)/len(arr)%1!=0 else int(sum(arr)/len(arr)))