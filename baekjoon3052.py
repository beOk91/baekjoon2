arr=[0]*42
cnt=0
for _ in range(10):
    num=int(input())%42
    if arr[num%42]==0:
        cnt+=1
    arr[num%42]+=1
print(cnt)