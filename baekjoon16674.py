n=input()
arr=[0]*5
for element in n:
    if element=="2":
        arr[0]+=1
    elif element=="0":
        arr[1]+=1
    elif element=="1":
        arr[2]+=1
    elif element=="8":
        arr[3]+=1
    else:
        arr[4]+=1

if arr[4]>0:
    print(0)
else:
    if arr[0]==arr[1] and arr[1]== arr[2] and arr[2]==arr[3]:
        print(8)
    elif arr[0]>0 and arr[1]>0 and arr[2]>0 and arr[3]>0:
        print(2)
    elif arr[0]>0 or arr[1]>0 or arr[2]>0 or arr[3]>0:
        print(1)