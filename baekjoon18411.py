arr=list(map(int,input().strip().split()))
arr.pop(arr.index(min(arr)))
print(sum(arr))