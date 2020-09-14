n=int(input())
arr={}
for _ in range(n):
    name=input()
    if arr.get(name)==None:arr[name]=1
    else:arr[name]+=1
arr=sorted(arr.items(),key=lambda x:(-x[1],x[0]))
print(arr[0][0])