result=0
arr=[]
for _ in range(4):
    a,b=map(int,input().strip().split())
    result=result-a+b
    arr.append(result)
print(max(arr))