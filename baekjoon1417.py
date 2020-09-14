n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
print(max(arr[1:])-arr[0])