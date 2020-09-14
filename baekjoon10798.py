arr=[]
for _ in range(5):
    arr.append(list(input().strip()))

for i in range(max(len(element) for element in arr)):
    for j in range(len(arr)):
        try:print(arr[j][i],end="")
        except:continue
