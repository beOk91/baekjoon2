arr1,arr2=[],[]
for _ in range(10):
    arr1.append(int(input()))
for _ in range(10):
    arr2.append(int(input()))
arr1.sort(reverse=True)
arr2.sort(reverse=True)
print(sum(arr1[0:3]),sum(arr2[0:3]))