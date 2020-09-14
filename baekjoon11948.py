arr,arr2=[],[]
for _ in range(4):
    arr.append(int(input()))
for _ in range(2):
    arr2.append(int(input()))
arr.pop(arr.index(min(arr)))
print(sum(arr)+max(arr2))