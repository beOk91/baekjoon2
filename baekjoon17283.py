l=int(input())
r=int(input())
result=l
arr=[]
while result>=5:
    result=int(result*(r/100))
    if result>5:arr.append(result)
print(sum(2**(i+1)*arr[i] for i in range(len(arr))))