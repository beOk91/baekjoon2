arr=[0]*6
for i in range(6):
    arr[i]=int(input())
print("A" if arr[0]*3+arr[1]*2+arr[2] > arr[3]*3+arr[4]*2+arr[5] else "B" if arr[0]*3+arr[1]*2+arr[2] < arr[3]*3+arr[4]*2+arr[5] else "T")