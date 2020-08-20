num=int(input())
arr=[]
for i in range(num):
    arr.append(int(input()))
for i in range(num):
    for j in range(num-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp

for i in range(num):
    print(arr[i])