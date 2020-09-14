while True:
    arr=list(map(int,input().strip().split()))
    arr.sort()
    if arr[0]==0 and arr[1]==0 and arr[2]==0:
        break
    if len(set(arr))==1:
        print("Equilateral")
    elif arr[2]>=arr[0]+arr[1]:
        print("Invalid")
    elif len(set(arr))==2:
        print("Isosceles")
    elif len(set(arr))==3:
        print("Scalene")