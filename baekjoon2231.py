num=int(input().strip())
arr=[0]*(num+1)
for i in range(1,num+1):
    arr[i]=i+sum(int(i) for i in str(i))
result=0
for i in range(len(arr)):
    if arr[i]==num:
        result=i;break
print(result)