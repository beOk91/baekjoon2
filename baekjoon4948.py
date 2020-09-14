arr=[False,False]+[True]*246910
for i in range(2,246911):
    for j in range(i+i,len(arr),i):
        if arr[j]:
            arr[j]=False
while True:
    num=int(input().strip())
    if num==0:break
    print(sum(1 if i else 0 for i in arr[(num+1):num*2+1]))