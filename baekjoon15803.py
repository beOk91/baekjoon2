arr=[]
for _ in range(3):
    arr.append(list(map(int,input().strip().split())))
if (arr[0][0] == arr[1][0] and arr[1][0] ==arr[2][0]) or (arr[0][1] == arr[1][1] and arr[1][1]==arr[2][1]):
    print("WHERE IS MY CHICKEN?")
else:
    print("WHERE IS MY CHICKEN?" if (arr[1][0]-arr[0][0])!=0 and (arr[2][0]-arr[0][0])!=0 and (arr[1][1]-arr[0][1])/(arr[1][0]-arr[0][0]) == (arr[2][1]-arr[0][1])/(arr[2][0]-arr[0][0]) else "WINNER WINNER CHICKEN DINNER!")
