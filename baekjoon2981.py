n=int(input())
m,arr=2,[]
for _ in range(n):
    arr.append(int(input()))
while m!=min(arr):
    val=True
    for i in range(len(arr)-1):
        if arr[i]%m!=arr[i+1]%m:
            val=False
            break
    if val:
        print(m,end=" ")
    m+=1