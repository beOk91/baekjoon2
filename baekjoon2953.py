arr=[[0]*5 for _ in range(5)]
arr2=[]
for i in range(5):
    arr=list(map(int,input().strip().split()))
    arr2.append(sum(arr))
print(arr2.index(max(arr2))+1,max(arr2))