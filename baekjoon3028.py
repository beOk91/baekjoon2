arr=[1,0,0]
text=input()
for element in text:
    if element=="A":
        arr[0],arr[1]=arr[1],arr[0]
    elif element=="B":
        arr[1],arr[2]=arr[2],arr[1]
    else:
        arr[0],arr[2]=arr[2],arr[0]
for i in range(len(arr)):
    if arr[i]>0:
        print(i+1)
