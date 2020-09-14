t=int(input())
sosu=[False,False]+[True]*9999
for i in range(2,9999):
    for j in range(i+i,len(sosu),i):
        if sosu[j]:sosu[j]=False
for _ in range(t):
    num=int(input())
    arr=[]
    for i in range(2,num//2+1):
        if sosu[i] and sosu[num-i]:
            arr.append([i,num-i])
    arr.sort(key=lambda x:x[1]-x[0])
    print(arr[0][0],arr[0][1])