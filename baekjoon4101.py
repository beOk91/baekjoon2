while True:
    arr=input().strip().split()
    if arr[0]=="0" and arr[1]=="0":
        break
    else:
        print("No" if int(arr[0])<=int(arr[1]) else "Yes")