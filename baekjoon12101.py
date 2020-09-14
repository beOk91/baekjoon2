n,k=map(int,input().strip().split())
result=[]
def f(num,arr):
    if sum(arr)==num:
        result.append(arr)
    if sum(arr)<num:
        for i in range(1,4):
            f(num,arr+[i])
f(n,[]);result.sort()
print("+".join(str(element) for element in result[k-1]) if k<=len(result) else -1)