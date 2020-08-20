arr=[]
for _ in range(7):
    num=int(input())
    if num%2!=0:
        arr.append(num)
arr.sort()
print(-1 if sum(arr)==0 else str(sum(arr))+"\n"+str(arr[0]))