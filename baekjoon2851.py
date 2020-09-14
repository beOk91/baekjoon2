arr=[]
result=[0]*10
for _ in range(10):
    arr.append(int(input()))
for i in range(10):
    mySum=0
    for j in range(i,10):
        mySum+=arr[j]
        if mySum>=100:
            mySum=(mySum-arr[j]) if 100-(mySum-arr[j])<= mySum-100 else mySum;break
    result[i]=100-mySum if 100-mySum>=0 else mySum-100
print(min(result)+100)