def f(idx,arr1,arr2):
    if idx==len(arr1):
        if len(arr2)==6:
            print(" ".join(str(element) for element in arr2))
        return
    f(idx+1,arr1,arr2+[arr1[idx]])
    f(idx+1,arr1,arr2)

while True:
    text=input().strip()
    if text=="0":break
    text=list(map(int,text.split()))
    f(0,text[1:],[])
    print()