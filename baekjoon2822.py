"""
arr=[]
for i in range(1,9):
    arr.append((i,int(input())))
arr.sort(key=lambda x:x[1])
print(sum(element[1] for element in arr[3:]))
arr=sorted(arr[3:], key=lambda x:x[0])
print(" ".join(str(element[0]) for element in arr))
"""
a=sorted([[int(input()),i] for i in range(1,9)])[3:]
k=1
for i in zip(*a):
    if k:
        print(sum(i))
        k-=1
    else:
        print(*sorted(i))