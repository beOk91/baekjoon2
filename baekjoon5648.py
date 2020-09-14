n=input().strip().split()
arr=[int(e[::-1]) for e in n[1:]]
while len(arr)!=int(n[0]):
    num=input().strip().split()
    arr=arr+[int(e[::-1]) for e in num]
arr.sort()
print("\n".join(str(e) for e in arr))