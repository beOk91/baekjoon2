n=int(input())
arr=[0]*2
for _ in range(n):
    a=int(input())
    arr[a]+=1
print("Junhee is not cute!" if arr[0]>arr[1] else "Junhee is cute!")