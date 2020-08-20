num=int(input())
text=input()
arr=[0]*2
for element in text:
    if element=="2":
        arr[0]+=1
    else:
        arr[1]+=1
print("yee" if arr[0]==arr[1] else (2 if arr[0]>arr[1] else "e"))