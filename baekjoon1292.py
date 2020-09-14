arr=[0]*1001
cnt,flag=1,False
for i in range(1,46):
    for j in range(i):
        arr[cnt]=i
        cnt+=1
        if cnt==1001:flag=True;break
    if flag:break
a,b=map(int,input().strip().split())
print(sum(i for i in arr[a:b+1]))
