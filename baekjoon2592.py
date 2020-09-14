arr=[0]*1001
cnt=0
for _ in range(10):
    num=int(input())
    cnt+=num
    arr[num]+=1
print(str(cnt//10)+"\n"+str(arr.index(max(arr))))