maxIndex=0
arr=[]
for i in range(9):
    arr.append(int(input()))
    if arr[i]>arr[maxIndex]:
        maxIndex=i
print(arr[maxIndex])
print(maxIndex+1)