n=int(input())
arr,cnt=[],1
for _ in range(n):
    arr.append(input())
while True:
    temp=[0]*n
    for i in range(len(arr)):
        temp[i]=int(arr[i])%int(10**cnt)
    if len(temp)==len(set(temp)):break
    cnt+=1
print(cnt)